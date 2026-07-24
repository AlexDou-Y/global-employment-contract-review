from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_report_evidence.py"
SPEC = importlib.util.spec_from_file_location("validate_report_evidence", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def build_report(
    *,
    include_difference_summary: bool = True,
    include_difference_table: bool = True,
    include_difference_evidence: bool = True,
) -> str:
    summary_row = ""
    if include_difference_summary:
        summary_row = (
            "| 是否存在需 HR 特别关注的当地法定差异 | "
            "存在1项，合同已覆盖但需纳入 Payroll 和预算 |\n"
        )

    difference_table = ""
    if include_difference_table:
        evidence = "[S1] [S2]" if include_difference_evidence else "待核验"
        difference_table = f"""
### 当地特殊法定机制及中外差异提示

| 事项 | 当地规则及中国差异 | 合同状态 | 雇主影响 | HR 动作 | 依据 |
|---|---|---|---|---|---|
| 发薪周期 | 当地法要求工资支付间隔不超过15日；中国对应全国性规则未设置相同周期 | 合同已覆盖 | Payroll 需按半月配置 | 验证发薪日历 | {evidence} |
"""

    return f"""# 示例劳动合同审核结果

## 一、总体结论

| 审核项目 | 结论 |
|---|---|
| 是否可以作为当地雇佣合同基础版本 | 可以 |
{summary_row}
{difference_table}
## 二、合同基础信息与审查假设

国家和工作地信息已确认。

## 三、风险总览

未发现需要升级处理的风险。

## 四、🔴 必须修改：明显违法或法定必备缺失条款

> 未发现需要单独列示的问题。

## 五、🟠 建议确认或调整：重要雇主风险 / 签前确认事项

> 未发现需要单独列示的问题。

## 六、🟡 建议完善：无明显违法但边界不清条款

> 未发现需要单独列示的问题。

## 七、🟢 建议补充：雇主保护条款

> 未发现需要单独列示的问题。

## 八、最终处理清单

无。

## 九、签署前待确认事项

无。

## 十、来源清单

| 编号 | 来源 | 类型 | 支持的判断 | 链接/文件 | 访问日期 |
|---|---|---|---|---|---|
| S1 | 当地官方劳动法 | 官方 | 当地发薪周期 | https://example.test/local | 2026-07-24 |
| S2 | 中国官方劳动法规 | 官方 | 中国规则对照 | https://example.test/china | 2026-07-24 |

## 附录：可以保留 / 暂不修改条款

无。
"""


def validate_text(text: str) -> list[str]:
    with tempfile.TemporaryDirectory() as temp_dir:
        report_path = Path(temp_dir) / "report.md"
        report_path.write_text(text, encoding="utf-8")
        return VALIDATOR.validate_report(report_path)


class LocalDifferenceValidationTests(unittest.TestCase):
    def test_requires_local_difference_summary_row(self) -> None:
        errors = validate_text(build_report(include_difference_summary=False))

        self.assertIn(
            "Missing overall conclusion row: `是否存在需 HR 特别关注的当地法定差异`.",
            errors,
        )

    def test_requires_local_difference_table(self) -> None:
        errors = validate_text(build_report(include_difference_table=False))

        self.assertIn(
            "Missing subsection: `### 当地特殊法定机制及中外差异提示`.",
            errors,
        )

    def test_requires_evidence_labels_in_local_difference_rows(self) -> None:
        errors = validate_text(build_report(include_difference_evidence=False))

        self.assertIn(
            "Local-difference row `发薪周期` lacks an [S#] evidence label.",
            errors,
        )

    def test_accepts_complete_local_difference_output(self) -> None:
        errors = validate_text(build_report())

        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
