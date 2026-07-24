# Risk Taxonomy

Use the actual risk symbols `🔴`, `🟠`, `🟡`, and `🟢` in report headings, tables, and action checklists. Do not output color words alone such as `红色`, `橙色`, `黄色`, or `绿色`.

## Severity Levels

| Symbol | Level | Use when | Action |
|---|---|---|---|
| 🔴 | 重大合规风险 | 明显违法、低于强制法定底线、法定必备条款重大缺失，或用工主体、工签、薪酬支付安排可能导致重大合规责任 | 必须修改 |
| 🟠 | 重要雇主风险 | 不一定违法，但可能导致补缴、罚款、解除受限、额外补偿、EOR责任不清，或形成高于法定的实质义务 | 建议确认或调整 |
| 🟡 | 一般条款风险 | 条款方向基本可接受，但表述不清、缺少必要限制或兜底、操作口径不完整、证据要求不足，可能造成执行争议或管理成本 | 建议完善 |
| 🟢 | 文件完善事项 / 雇主保护补充 | 不影响合同效力和核心雇主义务，主要是信息缺失、格式、版本、附件、签署流程、留档，或建议新增对雇主有利的保护性条款 | 建议补充 |

## Risk Categories

| Category | Meaning |
|---|---|
| Legal Compliance | Mandatory labor law, contract validity, statutory rights, local filing, language, employee classification |
| Payroll / Tax / Social Security | Wage payment, deductions, withholding, employer contributions, currency, payslip, tax equalization |
| Immigration / Work Authorization | Visa, work permit, right to work, cross-border remote work, illegal work exposure |
| Employer Cost | Above-statutory benefits, guaranteed bonus, commission, severance, allowances, insurance, repatriation |
| Employer Flexibility | Work location, duties, transfer, policy amendments, working time, termination, probation |
| Evidence / Enforceability | Ambiguous clauses, missing attachments, weak approval mechanism, unenforceable restrictive covenants |
| EOR / Vendor Risk | EOR role confusion, indemnity gaps, local employer duties, co-employment, vendor template conflicts |
| Data / Confidentiality / IP | Confidential information, personal data, invention assignment, IP ownership, post-employment duties |
| Political / Sovereignty Terminology | Country/region naming, Taiwan/Hong Kong/Macau wording, disputed territory references, government/legal-system names, public authority references, and external communication sensitivity |

## Dimension Markers

| Marker | Use when | Relationship to severity |
|---|---|---|
| ⚑ | Political, sovereignty, country/region, government, court, authority, or legal-system wording requires special review | Not a severity level; pair with 🔴/🟠/🟡/🟢 based on actual risk |

`当地特殊法定机制及中外差异` is also a review dimension, but it has no marker. A compliant local mechanism stays in the fixed summary table and does not receive a risk color merely because it differs from China.

## Employer-Unfavorable Clause Signals

Flag a clause even if it is lawful when it:

- makes bonus, commission, allowance, equity, remote work, relocation, or annual increase automatic;
- limits the employer's right to change policies, duties, reporting line, work location, or compensation plans;
- grants longer notice, severance, leave, sick pay, probation protection, or termination procedure than law requires;
- lacks employee obligations for visa, compliance documents, confidentiality, IP, return of property, or conflict of interest;
- gives employee unilateral resignation/termination rights without matching employer protections;
- imports a foreign law/forum that may be ineffective under mandatory local employment law;
- creates unclear EOR/client responsibilities or lets vendor template terms override company policy.
- uses political, sovereignty, country/region, government, or legal-system wording that may conflict with company naming standards, China-context governance requirements, external communication rules, or template-reuse expectations.

## Delta Risk Classification

Use this classification when the issue is a difference between contract language and statutory requirements:

| Delta type | Classification | Required explanation |
|---|---|---|
| Contract is below a mandatory statutory floor | 🔴 unless source support is uncertain | Identify the exact statutory floor and how the clause falls short |
| Contract grants more than the statutory minimum | 🟠 unless the business intentionally accepts it | State it is lawful but may create extra employer cost or reduced flexibility |
| Contract mixes amounts with different payment deadlines | 🔴 or 🟠 depending on wage-payment risk | Split earned wages, severance, unused leave payout, bonus/commission, expenses, equity, and contingent amounts |
| Contract uses a single fixed rule where law varies by condition | 🟠 or 🟡 | Show the statutory bands/triggers and where the fixed rule is unfavorable or unclear |
| Contract says "as required by law" but operational steps are missing | 🟡 unless a mandatory item is absent | List which HR/Payroll/Legal steps must be added |
| Contract complies with a material local rule that still affects budget or operations | No risk classification unless implementation is deficient | Keep the item in the local-difference summary and state the Payroll, budget, HR, or workforce action |
| Local-difference comparison lacks an official source on either the local or China side | No confirmed risk classification | Mark the item `待确认`; do not state that China has no equivalent rule |
| Contract uses political or sovereignty-sensitive terminology | 🟠 unless only translation consistency is affected | Separate local legal effectiveness from company acceptability; provide neutral wording or require Legal/local counsel confirmation |

Do not classify a lawful above-statutory benefit as "illegal". Describe it as an employer-side cost/flexibility issue and make the business choice explicit: accept the better benefit, narrow it, or revert to statutory minimum wording.

## Required Finding Fields

Each substantive issue must include:

- Clause location with page and section where available
- Original text excerpt or "原合同未约定。"
- Judgment
- Employer-side impact
- Modification recommendation
- Source labels such as `[S1]`
