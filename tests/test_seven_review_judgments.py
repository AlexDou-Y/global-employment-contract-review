import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SEVEN_JUDGMENTS = [
    "是否可以作为当地雇佣合同基础版本",
    "是否存在明显违法或低于法定底线的条款",
    "法定必备条款是否全面",
    "是否存在需签署前修改的雇主方风险",
    "是否存在高于法定权益 / 额外承诺",
    "是否存在 ⚑ 政治/主权/地域称谓敏感表述",
    "是否存在需 HR 特别关注的当地法定差异",
]


class SevenReviewJudgmentsTests(unittest.TestCase):
    def test_core_skill_defines_all_seven_mandatory_review_judgments(self):
        for relative_path in ["SKILL.md", "references/review-framework.md"]:
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("Seven Mandatory Review Judgments", text)
            for judgment in SEVEN_JUDGMENTS:
                self.assertIn(judgment, text)

    def test_readmes_describe_the_iteration_as_six_to_seven(self):
        zh = (ROOT / "README.zh.md").read_text(encoding="utf-8")
        en = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("从六项强制审核判断升级为七项", zh)
        self.assertIn("from six to seven mandatory review judgments", en)
        for judgment in SEVEN_JUDGMENTS:
            self.assertIn(judgment, zh)

    def test_report_requirements_and_template_use_all_seven_rows(self):
        for relative_path in [
            "references/output-requirements.md",
            "templates/contract-review-report.md",
        ]:
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            for judgment in SEVEN_JUDGMENTS:
                self.assertIn(judgment, text, relative_path)
    def test_obsolete_five_question_wording_is_removed(self):
        targets = [
            "SKILL.md",
            "references/review-framework.md",
            "README.zh.md",
            "README.md",
            "docs/introducing-global-employment-contract-review-skill.zh.md",
            "docs/introducing-global-employment-contract-review-skill.en.md",
        ]
        forbidden = [
            "Review five questions",
            "Five Mandatory Judgments",
            "five mandatory questions",
            "五项强制判断",
            "五个强制问题",
        ]

        for relative_path in targets:
            text = (ROOT / relative_path).read_text(encoding="utf-8")
            for phrase in forbidden:
                self.assertNotIn(phrase, text, relative_path)


if __name__ == "__main__":
    unittest.main()
