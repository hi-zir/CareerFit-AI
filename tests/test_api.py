import unittest

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


if __name__ == "__main__":
    unittest.main()
