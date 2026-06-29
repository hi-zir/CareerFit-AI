import unittest
from unittest.mock import patch

from fastapi.testclient import TestClient

from api.main import app


class TestApiRootEndpoint(unittest.TestCase):
    def test_root_endpoint_returns_api_status(self):
        client = TestClient(app)

        response = client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json(),
            {
                "app": "CareerFit AI",
                "version": "v2",
                "status": "running",
            },
        )
    def test_analyze_endpoint_returns_report(self):
        client = TestClient(app)
        fake_report = "# Fake CareerFit AI Match Report"

        with patch("api.main.analyze_resume_match", return_value=fake_report) as mock_analyze:
            response = client.post(
                "/analyze",
                json={
                    "resume_text": "Python and SQL resume",
                    "job_description_text": "Backend AI job",
                },
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"report": fake_report})

        mock_analyze.assert_called_once_with(
            resume_text="Python and SQL resume",
            job_description_text="Backend AI job",
        )

if __name__ == "__main__":
    unittest.main()
