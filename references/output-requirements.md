# Output Requirements

## Default Output

Produce one Markdown report. Do not generate `.docx`, spreadsheet, or slides unless the user asks.

## Style

- Use Simplified Chinese.
- Start with a direct one-sentence core judgment.
- Use compact tables for overall conclusions, risk distribution, final handling checklist, pending confirmations, sources, and appendix items.
- Use narrative clause review blocks for substantive clause analysis.
- Keep official-source citations as short labels in the body, such as `[S1]`, with full links in the source list.
- Keep legal uncertainty explicit. Do not give final legal sign-off.
- Use the exact fallback warning when no official source is found: `⚠️ 未检索到官方来源，以下基于模型知识库，需人工核实。`
- Do not over-expand background. Include only facts that affect signing, revision, or confirmation decisions.
- Apply `references/anti-hallucination-rules.md` before finalizing. Do not state unverified legal rules, numbers, official names, or contract facts as confirmed.

## Required Sections

1. **总体结论**
2. **合同基础信息与审查假设**
3. **风险总览**
4. **🔴 必须修改：明显违法或法定必备缺失条款**
5. **🟠 建议确认或调整：高于法定权益 / 额外承诺条款**
6. **🟡 建议完善：无明显违法但边界不清条款**
7. **🟢 建议补充：雇主保护条款**
8. **最终处理清单**
9. **签署前待确认事项**
10. **来源清单**
11. **附录：可以保留 / 暂不修改条款**

## Overall Conclusion Requirements

The "总体结论" table must show judgment plus count where relevant:

| 审核项目 | 结论 |
|---|---|
| 是否可以作为当地雇佣合同基础版本 | [可以 / 不建议 / 待确认] |
| 是否存在明显违法或低于法定底线的条款 | [未发现 / 存在X项 / 待确认X项] |
| 法定必备条款是否全面 | [全面 / 基本全面但需补充X项 / 不全面，缺失X项 / 待确认X项] |
| 是否存在需签署前修改的雇主方风险 | [存在X项，其中签署前建议优先处理X项 / 不存在 / 待确认X项] |
| 是否存在高于法定权益 / 额外承诺 | [存在X项 / 不存在 / 待确认X项] |

Counting rules:

- "明显违法或低于法定底线" counts 🔴 findings.
- "需签署前修改的雇主方风险" may count 🔴 + 🟠 + key 🟡 findings.
- "高于法定权益 / 额外承诺" counts only findings that grant above-statutory employee rights or company extra commitments.
- "法定必备条款是否全面" counts missing or confirmation-needed mandatory content, not general wording improvements.

## Risk Overview Requirements

In "风险总览", do not create separate `3.1` and `3.2` subsections. Put a compact risk-level explanation first, then the contract-specific risk distribution table.

Use this wording pattern:

```markdown
> **风险等级说明：**  
> 🔴 **重大合规风险**：明显违法、低于强制法定底线、法定必备条款重大缺失，或可能导致重大合规责任。处理动作：**必须修改**。  
> 🟠 **重要雇主风险**：不一定违法，但可能导致补缴、罚款、解除受限、额外补偿，或形成高于法定的实质义务。处理动作：**建议确认或调整**。  
> 🟡 **一般条款风险**：条款方向基本可接受，但边界、证据、审批或兜底不清，可能造成执行争议或管理成本。处理动作：**建议完善**。  
> 🟢 **文件完善事项 / 雇主保护补充**：主要是信息、格式、附件、签署、留档，或建议新增对雇主有利的保护性条款。处理动作：**建议补充**。
```

Then add:

| 风险等级 | 数量 | 主要问题 | 处理动作 |
|---|---:|---|---|
| 🔴 重大合规风险 | [0] | [ ] | 必须修改 |
| 🟠 重要雇主风险 | [0] | [ ] | 建议确认或调整 |
| 🟡 一般条款风险 | [0] | [ ] | 建议完善 |
| 🟢 文件完善事项 / 雇主保护补充 | [0] | [ ] | 建议补充 |

## Clause Review Rules

- Put substantive findings only in Sections 4-7.
- If there are no findings under a section, state `未发现需要单独列示的问题。`
- Each finding must have its own numbered heading, such as `### 6.2 final salary 表述过窄`.
- Headings must describe the actual issue, not only the clause category.
- Do not combine unrelated issues under one heading.
- Each clause block must use exactly these fields:
  - 条款位置
  - 原文内容
  - 问题判断
  - 雇主影响
  - 修改建议
  - 依据

## Final Handling Checklist

Use one table only:

| 序号 | 优先级 | 条款位置 | 条款/问题 | 处理动作 | 责任方 | 签署前是否必须完成 |
|---:|---|---|---|---|---|---|
| 1 | 🔴 必须修改 | [第X页 / 第X条] | [问题] | [删除 / 改写 / 补充 / 签前确认] | [HR / Legal / EOR / Payroll] | 是 |
| 2 | 🟠 建议确认或调整 | [第X页 / 第X条] | [问题] | [确认是否接受 / 弱化 / 加条件] | [HR / Legal] | 视情况 |
| 3 | 🟡 建议完善 | [第X页 / 第X条] | [问题] | [补充边界 / 增加兜底 / 调整表述] | [HR / Legal] | 否，但建议签前完成 |
| 4 | 🟢 建议补充 | [新增条款] | [问题] | [新增保护条款] | [HR / Legal] | 否，但建议签前完成 |

Do not include "可以保留 / 暂不修改" in this action checklist. Put those items in the appendix.

## Pending Confirmation

Use the title **签署前待确认事项**. This section is for issues that cannot be finally concluded from the contract and public sources alone and require Legal, local counsel, EOR, Payroll, Tax, visa vendor, or business owner confirmation.

## Visual Conventions

| Symbol | Meaning |
|---|---|
| 🔴 | 重大合规风险 |
| 🟠 | 重要雇主风险 |
| 🟡 | 一般条款风险 |
| 🟢 | 文件完善事项 / 雇主保护补充 |
| ✅ | No material issue found based on available sources |
| ⚠️ | Missing fact, missing source, or manual confirmation needed |
| 📌 | Recommended HR action |

## Source Type Legend

Use this legend before the source list:

| 来源类型 | 含义 |
|---|---|
| 官方 | 政府、监管机构、法院、官方法律数据库 |
| EOR / Vendor | EOR、Payroll、签证供应商等服务商说明 |
| 律所 / 专业机构 | 律所、会计师事务所、咨询机构资料 |
| 降级提示 | 未检索到官方来源，基于模型知识库，需人工核实 |

## Hallucination Self-Check

Before final delivery, verify:

- every finding in Sections 4-7 has all six required fields;
- every finding has contract evidence and an evidence label in `依据`;
- every `[S#]` label used in findings appears in the source list;
- each cited source supports the exact judgment;
- no non-official source is labelled as official;
- no unverified statutory number, amount, rate, day count, article number, or official name is stated as fact;
- no placeholder such as `[ ]`, `TBD`, or `TODO` remains in the final report;
- uncertain issues are listed in `签署前待确认事项`;
- the report does not use over-certain phrases such as `完全合规`, `无风险`, `一定合法`, `保证合规`, or `无需进一步确认`.
