import tempfile
import unittest
from pathlib import Path

from app import read_text_file
from prompts import build_resume_match_prompt
from services.resume_matcher import analyze_resume_match


class TestCoreAppFunctions(unittest.TestCase):
    def test_read_text_file_returns_file_content(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            file_path = Path(temp_dir) / "sample.txt"
            file_path.write_text("Hello CareerFit AI", encoding="utf-8")

            result = read_text_file(file_path)

            self.assertEqual(result, "Hello CareerFit AI")

    def test_read_text_file_raises_error_for_missing_file(self):
        missing_file = Path("missing_file.txt")

        with self.assertRaises(FileNotFoundError):
            read_text_file(missing_file)


class TestPromptBuilder(unittest.TestCase):
    def test_prompt_includes_honesty_rules(self):
        prompt = build_resume_match_prompt(
            resume_text="Python and SQL experience.",
            job_description_text="Backend role with Python and APIs.",
        )

        self.assertIn("Do not invent metrics", prompt)
        self.assertIn("[insert real metric]", prompt)
        self.assertIn("Only Add If True", prompt)


class TestResumeMatcherValidation(unittest.TestCase):
    def test_empty_resume_raises_error(self):
        with self.assertRaises(ValueError):
            analyze_resume_match("", "Job description text")

    def test_empty_job_description_raises_error(self):
        with self.assertRaises(ValueError):
            analyze_resume_match("Resume text", "")


if __name__ == "__main__":
    unittest.main()
