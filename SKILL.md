---
name: global-employment-contract-review
description: Use when reviewing overseas employment contracts or Offer Letters from an employer-side HR compliance perspective, especially when country-specific mandatory terms, employee entitlements, employer-unfavorable clauses, official legal sources, Markdown audit reports, or Legal/EOR/vendor confirmation items are needed.
---

# Global Employment Contract Review

## Overview

Review overseas employment contracts and Offer Letters from the employer-side HR compliance perspective, based on practical experience reviewing employment contracts across multiple countries and regions. Prioritize whether the document is lawful, complete under local mandatory contract requirements, more generous than statutory minimums, or unfavorable to the employer.

Use Simplified Chinese by default. Output a Markdown report only unless the user explicitly requests another format.

## Mandatory Rules

- Treat the company as the review client: identify employer risk, operational burden, approval needs, and clauses that weaken employer control.
- Do not give final legal sign-off. Mark high-risk legal, tax, visa, social security, termination, restrictive covenant, or benefits issues as requiring Legal, Tax/Finance, EOR provider, vendor, or local counsel confirmation.
- Cite a source for every risk finding. Prefer official laws, government guidance, regulator pages, court/labor authority materials, or official gazettes.
- Do not invent laws, article numbers, official institution names, statutory amounts, statutory days, rates, visa rules, or contract facts. Read `references/anti-hallucination-rules.md` for evidence and uncertainty rules.
- If no official source is found, write exactly: `⚠️ 未检索到官方来源，以下基于模型知识库，需人工核实。`
- Distinguish statutory risk from employer-commercial disadvantage. A lawful clause may still be unfavorable to the employer.
- Review political, sovereignty, and country/region terminology as a separate employer-side governance issue. Read `references/political-sovereignty-terminology.md` when the contract mentions Taiwan, Hong Kong, Macau, disputed territories, country lists, government names, governing law, jurisdiction, public authorities, or legal-system names.
- If country/region, employee type, legal employer, actual work location, or governing law is unclear, proceed conditionally and list the missing facts in the report.

## Workflow

1. **Scope the scenario**
   - Identify country/region, employee type, employment model, legal employer, work location, governing law, payroll location, visa/work authorization, and document type.
   - Read `references/review-framework.md` for the mandatory review sequence.

2. **Extract contract facts**
   - Extract clauses and facts before judging them.
   - If useful, run `scripts/extract_contract_text.py` to extract plain text from `.docx`, `.pdf`, `.txt`, or `.md`.
   - Compare internal consistency across the contract, annexes, offer letter, and any employee baseline information.
   - Scan political, sovereignty, and country/region terminology in parties, governing law, jurisdiction, work location, payroll/tax/social security, immigration, annexes, and signature blocks.

3. **Build the legal baseline**
   - Use official sources first. Read `references/source-verification-rules.md`.
   - Read `references/anti-hallucination-rules.md` before making country-specific legal assertions.
   - For a new jurisdiction, use `references/country-rule-template.md` to structure a country rule card.
   - Do not invent statutory rules, official English names, or salary/benefit benchmarks.

4. **Evidence lock**
   - Separate contract facts from legal/source findings before drafting conclusions.
   - For each planned finding, confirm the contract evidence: page, section, and short original excerpt.
   - For each legal or compliance judgment, confirm the supporting source label, such as `[S1]`, and verify the source actually supports the judgment.
   - If no official source is found, use the exact fallback warning and move the point to "签署前待确认事项" when needed.
   - Do not write uncertain facts as confirmed findings.

5. **Assess risks**
   - Review four questions for each topic:
     1. Is the clause illegal, invalid, or non-compliant?
     2. Does the document include all mandatory local employment contract contents?
     3. Does the contract grant employee rights above statutory minimums?
     4. Does the clause create employer-unfavorable cost, flexibility, evidence, enforcement, or termination risk?
   - For political or sovereignty-sensitive wording, separate local legal effectiveness from China-context company acceptability. Do not label the wording locally invalid without a supporting source; instead flag it as employer-side governance, approval, external communication, or template-reuse risk.
   - Use `references/risk-taxonomy.md` for severity and classification.

6. **Write the Markdown report**
   - Use `templates/contract-review-report.md`.
   - Read `references/output-requirements.md` before drafting the report.
   - Start with a concise core judgment that states whether the contract can be used as a base version and the main signing-before-change points.
   - Use this fixed top-level structure: 总体结论, 合同基础信息与审查假设, 风险总览, 🔴 必须修改, 🟠 建议确认或调整, 🟡 建议完善, 🟢 建议补充, 最终处理清单, 签署前待确认事项, 来源清单, 附录：可以保留 / 暂不修改条款.
   - Classify every substantive finding into one of four top-level sections:
     - 🔴 必须修改：明显违法或法定必备缺失条款
     - 🟠 建议确认或调整：重要雇主风险 / 签前确认事项，包括高于法定权益、额外承诺、政治/主权/地域称谓敏感表述、治理审批风险、EOR/客户职责不清等
     - 🟡 建议完善：无明显违法但边界不清条款
     - 🟢 建议补充：雇主保护条款
   - Use `⚑` as a dimension marker for political, sovereignty, or country/region-sensitive wording. `⚑` is not a risk level; pair it with `🔴/🟠/🟡/🟢` when severity is needed.
   - Use narrative clause review blocks for substantive issues instead of P0/P1 issue cards or wide risk tables.
   - Give every finding its own numbered heading, such as `### 5.1 公司解除需有 objective reason only`; do not combine unrelated findings under one heading.
   - Each substantive clause block must use these exact fields: 条款位置, 原文内容, 问题判断, 雇主影响, 修改建议, 依据.
   - The final handling checklist must be one action table, not separate tables by risk level.
   - Put "可以保留 / 暂不修改" items in the appendix only, not in the action checklist.
   - Put full source links only in the source list at the end.
   - Include a "签署前待确认事项" section for unresolved legal, tax, visa, payroll, EOR, or factual questions.

7. **Hallucination self-check before finalizing**
   - Read the checklist in `references/anti-hallucination-rules.md`.
   - Verify every risk finding has a source or the required no-official-source warning.
   - Verify every source label in a finding appears in the source list and supports the exact judgment.
   - If a report file is generated locally, run `scripts/validate_report_evidence.py <report.md>` before final delivery.
   - Verify the report is actionable for HR, Legal, Finance, EOR/vendor, or the business owner.
   - Verify the final output is Markdown and does not overstate legal certainty.

## Reference Map

| Need | Load |
|---|---|
| End-to-end review sequence | `references/review-framework.md` |
| Severity, risk categories, symbols | `references/risk-taxonomy.md` |
| Political, sovereignty, and country/region terminology | `references/political-sovereignty-terminology.md` |
| Official source hierarchy and fallback language | `references/source-verification-rules.md` |
| Anti-hallucination evidence and uncertainty rules | `references/anti-hallucination-rules.md` |
| Creating country-specific rule cards | `references/country-rule-template.md` |
| Markdown output requirements | `references/output-requirements.md` |
| Full report skeleton | `templates/contract-review-report.md` |
| Issue table snippet | `templates/issue-list-table.md` |
| Country rule card template | `templates/country-rule-card.md` |

## Common Mistakes

| Mistake | Required correction |
|---|---|
| Reviewing from the employee's benefit perspective only | Reframe as employer-side HR compliance and risk control |
| Saying "compliant" without country facts | State assumptions and missing facts first |
| Listing risks without sources | Add official source or the required fallback warning |
| Citing a source that is only topically related | Verify the source supports the exact legal or factual judgment |
| Treating model inference as a fact | Mark it as an assumption or move it to 签署前待确认事项 |
| Using exact statutory numbers without verification | Verify with an official source or mark for confirmation |
| Putting all risks in one wide table | Use one numbered heading and one fixed-field review block for each finding |
| Repeating the same issue in every section | Put the full analysis once, then cross-reference briefly |
| Over-fragmenting the report into too many risk cards | Group substantive issues into the four risk-level sections: 🔴, 🟠, 🟡, 🟢 |
| Replacing risk symbols with color words | Use `🔴`, `🟠`, `🟡`, and `🟢` in headings, risk tables, and action checklists; do not write only `红色/橙色/黄色/绿色` |
| Treating every important employer risk as "must revise" | Use "建议确认或调整" when the issue is lawful but creates extra employer obligation or cost |
| Mixing "可以保留" items into the action checklist | Put them in the appendix only |
| Saying "above statutory" or "below statutory" without explaining the delta | Add a compact comparison table or scenario breakdown showing statutory rule vs contract language vs employer impact |
| Mixing final wage, severance, unused leave payout, bonus/commission, expenses, and equity into one payment-timing finding | Split payment types and identify the legal or policy deadline for each |
| Treating EOR as risk-free | Check EOR role, employer obligations, indemnity gaps, and local mandatory law |
| Ignoring generous clauses | Flag above-statutory entitlements and employer cost/control impact |
| Ignoring politically sensitive country/region wording because it is not a labor-law issue | Flag it separately as employer-side governance and approval risk; confirm neutral wording with Legal/local counsel |
| Giving final legal advice | Convert to HR recommendation plus Legal/local counsel confirmation item |
