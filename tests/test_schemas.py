import unittest

from pydantic import ValidationError

from api.schemas import ResumeMatchRequest, ResumeMatchResponse


class TestApiSchemas(unittest.TestCase):
    def test_resume_match_request_accepts_valid_data(self):
        request = ResumeMatchRequest(
            resume_text="Python and SQL resume",
            job_description_text="Backend AI job",
        )

        self.assertEqual(request.resume_text, "Python and SQL resume")
        self.assertEqual(request.job_description_text, "Backend AI job")

    def test_resume_match_request_rejects_empty_resume(self):
        with self.assertRaises(ValidationError):
            ResumeMatchRequest(
                resume_text="",
                job_description_text="Backend AI job",
            )

    def test_resume_match_request_rejects_empty_job_description(self):
        with self.assertRaises(ValidationError):
            ResumeMatchRequest(
                resume_text="Python and SQL resume",
                job_description_text="",
            )

    def test_resume_match_response_accepts_report(self):
        """
        Verifies that the API response schema accepts a report, summary,
        and an optional match score.
        """
        response = ResumeMatchResponse(
            report="# CareerFit AI Match Report",
            summary="CareerFit AI analysis completed successfully.",
            match_score=75,
        )

        self.assertEqual(response.report, "# CareerFit AI Match Report")
        self.assertEqual(
            response.summary,
            "CareerFit AI analysis completed successfully.",
        )
        self.assertEqual(response.match_score, 75)
    
    def test_resume_match_response_allows_missing_match_score(self):
        """
        Verifies that match_score can be missing because the current AI
        workflow returns a Markdown report instead of structured JSON.
        """
        response = ResumeMatchResponse(
            report="# CareerFit AI Match Report",
            summary="CareerFit AI analysis completed successfully.",
        )

        self.assertIsNone(response.match_score)    


if __name__ == "__main__":
    unittest.main()
