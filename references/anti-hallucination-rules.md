# Anti-Hallucination Rules

## Never Invent

Do not invent:

- law names, article numbers, official institution names, official English translations, statutory amounts, statutory days, statutory rates, minimum wages, social security rates, tax rates, visa rules, or filing requirements;
- contract facts that are not in the contract, annexes, offer letter, employee baseline information, or user-provided context;
- source authority, such as calling an EOR page, law firm update, blog, or AI summary an official source;
- final legal conclusions where the facts or official sources are incomplete.

## Evidence Binding

Every substantive finding must bind two kinds of evidence:

1. **Contract evidence**: page, section, clause title, and short original excerpt. If the issue is a missing employer-protection clause, write `原合同未约定。`
2. **Rule/source evidence**: source label such as `[S1]`, a cited internal file, contract text, or the required no-official-source fallback.

The cited source must support the exact judgment being made. A merely related source is not enough.

## Uncertainty Labels

Use cautious language when facts or official sources are incomplete:

- `待确认`
- `需 Legal / local counsel / EOR / Payroll / Tax / Visa vendor 确认`
- `基于现有合同文本暂未发现`
- `如适用 [Award / agreement / local law]，需另行核验`
- `根据现有公开来源，初步判断为...`

Avoid definitive wording unless directly supported by reliable sources:

- `完全合规`
- `无风险`
- `一定合法`
- `一定违法`
- `保证合规`
- `无需进一步确认`

## Official Source Missing

If no official source is found, write exactly:

`⚠️ 未检索到官方来源，以下基于模型知识库，需人工核实。`

Then:

- avoid final legal wording;
- mark the issue for manual confirmation if it affects legality, cost, visa, tax, social security, termination, restrictive covenants, or contract validity;
- identify who should confirm the point.

## Hallucination Self-Check

Before finalizing a report, verify:

- every finding in Sections 4-7 has `条款位置`, `原文内容`, `问题判断`, `雇主影响`, `修改建议`, and `依据`;
- every legal or compliance judgment has a source label, cited internal file, contract evidence, or the exact fallback warning;
- every source label used in Sections 4-7 appears in the source list;
- every cited source supports the exact judgment, not only the general topic;
- no non-official source is described as official;
- no unverified statutory number, amount, rate, day count, article number, or official name is stated as fact;
- no placeholder such as `[ ]`, `TBD`, or `TODO` remains in a final report;
- no uncertain issue is presented as a confirmed conclusion;
- unresolved facts are listed in `签署前待确认事项`.

