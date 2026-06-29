import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app import run_analysis


class TestAppWorkflow(unittest.TestCase):
    def test_run_analysis_reads_inputs_and_saves_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            resume_path = temp_path / "resume.txt"
            job_path = temp_path / "job.txt"
            output_path = temp_path / "report.md"

            resume_path.write_text("Python and SQL resume", encoding="utf-8")
            job_path.write_text("Python backend job", encoding="utf-8")

            fake_report = "# Fake CareerFit Report"

            with patch("app.analyze_resume_match", return_value=fake_report) as mock_analyze:
                result = run_analysis(
                    resume_path=resume_path,
                    job_description_path=job_path,
                    output_path=output_path,
                )

            self.assertEqual(result, fake_report)
            self.assertEqual(output_path.read_text(encoding="utf-8"), fake_report)

            mock_analyze.assert_called_once_with(
                resume_text="Python and SQL resume",
                job_description_text="Python backend job",
            )


if __name__ == "__main__":
    unittest.main()
