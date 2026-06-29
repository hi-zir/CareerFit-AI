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
        response = ResumeMatchResponse(
            report="# CareerFit AI Match Report",
            summary="CareerFit AI analysis completed successfully.",
        )

        self.assertEqual(response.report, "# CareerFit AI Match Report")
        self.assertEqual(
            response.summary,
            "CareerFit AI analysis completed successfully.",
        )


if __name__ == "__main__":
    unittest.main()
