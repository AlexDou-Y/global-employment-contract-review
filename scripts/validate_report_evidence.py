#!/usr/bin/env python3
"""Validate evidence hygiene in an employment contract review report.

This is a mechanical check. It does not decide whether the legal analysis is
correct; it catches missing fields, missing citations, unresolved placeholders,
and over-certain wording that commonly causes audit issues.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FIELDS = [
    "条款位置",
    "原文内容",
    "问题判断",
    "雇主影响",
    "修改建议",
    "依据",
]

SECTION_RE = re.compile(r"^##\s+([四五六七])、", re.MULTILINE)
NEXT_SECTION_RE = re.compile(r"^##\s+", re.MULTILINE)
FINDING_RE = re.compile(r"^###\s+([4567]\.\d+)\s+(.+)$", re.MULTILINE)
SOURCE_DEF_RE = re.compile(r"^\|\s*(S\d+)\s*\|", re.MULTILINE)
SOURCE_USE_RE = re.compile(r"\[(S\d+)\]")
PLACEHOLDER_RE = re.compile(r"\[\s*\]|TBD|TODO|\[第X页|\[条款|\[问题|\[原因|\[来源|\[YYYY", re.IGNORECASE)
OVER_CERTAIN_TERMS = [
    "完全合规",
    "无风险",
    "一定合法",
    "保证合规",
    "无需进一步确认",
]
EVIDENCE_FALLBACK = "⚠️ 未检索到官方来源，以下基于模型知识库，需人工核实。"
LOCAL_DIFFERENCE_SUMMARY_LABEL = "是否存在需 HR 特别关注的当地法定差异"
LOCAL_DIFFERENCE_HEADING = "### 当地特殊法定机制及中外差异提示"
LOCAL_DIFFERENCE_TABLE_HEADER = [
    "事项",
    "当地规则及中国差异",
    "合同状态",
    "雇主影响",
    "HR 动作",
    "依据",
]
LOCAL_DIFFERENCE_STATUSES = {
    "与法律冲突", "缺少法定必备内容", "法律直接适用但合同未明确", "合同已覆盖", "待确认"
}


def line_no(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def extract_review_area(text: str) -> str:
    start = SECTION_RE.search(text)
    if not start:
        return ""
    end = re.search(r"^##\s+八、", text[start.start():], re.MULTILINE)
    if end:
        return text[start.start() : start.start() + end.start()]
    return text[start.start():]


def iter_findings(review_area: str):
    matches = list(FINDING_RE.finditer(review_area))
    for i, match in enumerate(matches):
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(review_area)
        yield match, review_area[start:end]


def extract_local_difference_area(text: str) -> str:
    start = text.find(LOCAL_DIFFERENCE_HEADING)
    if start == -1:
        return ""
    body_start = start + len(LOCAL_DIFFERENCE_HEADING)
    remainder = text[body_start:]
    end = re.search(r"^#{2,3}\s+", remainder, re.MULTILINE)
    if end:
        return text[start : body_start + end.start()]
    return text[start:]


def iter_local_difference_rows(area: str) -> list[list[str]]:
    lines = area.splitlines()
    expected_header = "| " + " | ".join(LOCAL_DIFFERENCE_TABLE_HEADER) + " |"
    header_index = next(
        (index for index, line in enumerate(lines) if line.strip() == expected_header),
        None,
    )
    if header_index is None:
        return []

    rows: list[list[str]] = []
    for line in lines[header_index + 1 :]:
        stripped = line.strip()
        if not stripped:
            if rows:
                break
            continue
        if not stripped.startswith("|"):
            if rows:
                break
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(re.fullmatch(r":?-+:?", cell) for cell in cells):
            continue
        rows.append(cells)
    return rows


def validate_report(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if f"| {LOCAL_DIFFERENCE_SUMMARY_LABEL} |" not in text:
        errors.append(
            f"Missing overall conclusion row: `{LOCAL_DIFFERENCE_SUMMARY_LABEL}`."
        )

    local_difference_area = extract_local_difference_area(text)
    if not local_difference_area:
        errors.append(f"Missing subsection: `{LOCAL_DIFFERENCE_HEADING}`.")
        local_difference_rows: list[list[str]] = []
    else:
        local_difference_rows = iter_local_difference_rows(local_difference_area)
        if not local_difference_rows:
            errors.append("Missing or empty local-difference table.")

    review_area = extract_review_area(text)
    if not review_area:
        errors.append("Missing Sections 4-7 review area.")
        return errors

    findings = list(iter_findings(review_area))
    if not findings and "未发现需要单独列示的问题。" not in review_area:
        errors.append("No findings found and no empty-section statement found.")

    defined_sources = set(SOURCE_DEF_RE.findall(text))
    used_sources = set(SOURCE_USE_RE.findall(review_area))
    used_sources.update(SOURCE_USE_RE.findall(local_difference_area))

    for src in sorted(used_sources - defined_sources):
        errors.append(f"Source label [{src}] is used in findings but missing from source list.")

    for cells in local_difference_rows:
        if len(cells) != len(LOCAL_DIFFERENCE_TABLE_HEADER):
            errors.append(
                "Local-difference table row must contain exactly six columns."
            )
            continue

        topic, _, status, _, _, evidence = cells
        if status not in LOCAL_DIFFERENCE_STATUSES:
            errors.append(
                f"Local-difference row `{topic}` uses unsupported contract status `{status}`."
            )

        source_labels = set(SOURCE_USE_RE.findall(evidence))
        if not source_labels:
            errors.append(
                f"Local-difference row `{topic}` lacks an [S#] evidence label."
            )
        elif status != "待确认" and len(source_labels) < 2:
            errors.append(
                f"Local-difference row `{topic}` requires at least two [S#] evidence "
                "labels for local and China baselines."
            )

    for match, body in findings:
        finding_id = match.group(1)
        title = match.group(2).strip()
        base = f"{finding_id} {title}"

        for field in REQUIRED_FIELDS:
            if f"**{field}：**" not in body:
                errors.append(f"{base}: missing required field `{field}`.")

        evidence_line = ""
        for line in body.splitlines():
            if line.startswith("**依据：**"):
                evidence_line = line
                break

        has_source = bool(SOURCE_USE_RE.search(evidence_line))
        has_contract_text = "合同文本" in evidence_line
        has_fallback = EVIDENCE_FALLBACK in body or "降级提示" in evidence_line
        if not (has_source or has_contract_text or has_fallback):
            errors.append(f"{base}: `依据` lacks [S#], 合同文本, or required fallback warning.")

    for match in PLACEHOLDER_RE.finditer(text):
        errors.append(f"Placeholder remains at line {line_no(text, match.start())}: `{match.group(0)}`.")

    for term in OVER_CERTAIN_TERMS:
        idx = text.find(term)
        if idx != -1:
            errors.append(f"Over-certain wording at line {line_no(text, idx)}: `{term}`.")

    if "## 九、签署前待确认事项" not in text:
        errors.append("Missing section: `## 九、签署前待确认事项`.")
    if "## 十、来源清单" not in text:
        errors.append("Missing section: `## 十、来源清单`.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate evidence hygiene in a Markdown contract review report.")
    parser.add_argument("report", help="Path to the Markdown report to validate")
    args = parser.parse_args()

    path = Path(args.report)
    if not path.exists():
        print(f"Report not found: {path}", file=sys.stderr)
        return 2

    errors = validate_report(path)
    if errors:
        print("Evidence validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Evidence validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
