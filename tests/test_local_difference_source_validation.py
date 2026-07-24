from __future__ import annotations

import unittest

from tests.test_validate_report_evidence import build_report, validate_text


class LocalDifferenceSourceValidationTests(unittest.TestCase):
    def test_confirmed_comparison_requires_two_source_labels(self) -> None:
        report = build_report().replace("[S1] [S2]", "[S1]", 1)

        errors = validate_text(report)

        self.assertIn(
            "Local-difference row `发薪周期` requires at least two [S#] evidence labels "
            "for local and China baselines.",
            errors,
        )

    def test_rejects_unknown_contract_status(self) -> None:
        report = build_report().replace("| 合同已覆盖 |", "| 可保留 |", 1)

        errors = validate_text(report)

        self.assertIn(
            "Local-difference row `发薪周期` uses unsupported contract status `可保留`.",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
