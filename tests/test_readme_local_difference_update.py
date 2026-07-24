import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ReadmeLocalDifferenceUpdateTests(unittest.TestCase):
    def test_chinese_readme_documents_2026_07_24_iteration(self):
        text = (ROOT / "README.zh.md").read_text(encoding="utf-8")

        required = [
            "| 2026.07.24 |",
            "## 本次更新说明（2026.07.24）",
            "七项强制审核判断",
            "当地特殊法定机制及中外差异",
            "是否存在需 HR 特别关注的当地法定差异",
            "事项 | 当地规则及中国差异 | 合同状态 | 雇主影响 | HR 动作 | 依据",
            "与法律冲突",
            "合同已覆盖",
            "待确认",
            "不得超过15日",
            "不等同于强制每14日",
            "不是新的风险等级",
            "### 当地特殊法定机制及中外差异提示",
            "已经确认的中外差异必须同时具有当地和中国规则依据",
            "test_readme_local_difference_update.py",
            "test_seven_review_judgments.py",
        ]

        for marker in required:
            self.assertIn(marker, text)

    def test_english_readme_documents_2026_07_24_iteration(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")

        required = [
            "| 2026.07.24 |",
            "## Update Notes (2026.07.24)",
            "seven mandatory review judgments",
            "local mandatory mechanisms and China comparison",
            "是否存在需 HR 特别关注的当地法定差异",
            "事项 | 当地规则及中国差异 | 合同状态 | 雇主影响 | HR 动作 | 依据",
            "与法律冲突",
            "合同已覆盖",
            "待确认",
            "no more than 15 days",
            "does not mean a mandatory 14-day biweekly cycle",
            "not a new risk level",
            "### 当地特殊法定机制及中外差异提示",
            "confirmed local-versus-China comparison must cite both the local and China legal baselines",
            "test_readme_local_difference_update.py",
            "test_seven_review_judgments.py",
        ]

        for marker in required:
            self.assertIn(marker, text)


if __name__ == "__main__":
    unittest.main()
