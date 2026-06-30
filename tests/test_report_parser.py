import unittest

from services.report_parser import extract_match_score


class TestReportParser(unittest.TestCase):
    """
    Tests for helper functions that parse structured values from AI reports.
    """

    def test_extract_match_score_from_score_out_of_100(self):
        """
        Verifies that the parser can extract a score written as 72/100.
        """
        report_text = """
        # CareerFit AI Match Report

        ## 1. Match Score
        Score: 72/100
        """

        score = extract_match_score(report_text)

        self.assertEqual(score, 72)

    def test_extract_match_score_from_match_score_number(self):
        """
        Verifies that the parser can extract a score written after
        the phrase "Match Score".
        """
        report_text = """
        # CareerFit AI Match Report

        ## 1. Match Score
        Match Score: 85
        """

        score = extract_match_score(report_text)

        self.assertEqual(score, 85)

    def test_extract_match_score_returns_none_when_missing(self):
        """
        Verifies that the parser returns None when no clear score exists.
        """
        report_text = """
        # CareerFit AI Match Report

        This report does not contain a clear numeric score.
        """

        score = extract_match_score(report_text)

        self.assertIsNone(score)

    def test_extract_match_score_rejects_score_above_100(self):
        """
        Verifies that the parser rejects impossible scores above 100.
        """
        report_text = "Score: 120/100"

        score = extract_match_score(report_text)

        self.assertIsNone(score)


if __name__ == "__main__":
    unittest.main()