import re
from typing import Optional


def extract_match_score(report_text: str) -> Optional[int]:
    """
    Extracts a resume/job match score from an AI-generated Markdown report.

    The current AI report is plain text, so this function looks for common
    score patterns such as "Score: 72/100" or "Match Score: 85".

    Args:
        report_text (str): The AI-generated report text.

    Returns:
        Optional[int]: The extracted score from 0 to 100, or None if no
        clear score is found.
    """
    score_patterns = [
        r"score\s*[:\-]?\s*(\d{1,3})\s*/\s*100",
        r"match score\s*[:\-]?\s*(\d{1,3})",
    ]

    for pattern in score_patterns:
        match = re.search(pattern, report_text, re.IGNORECASE)

        if match:
            score = int(match.group(1))

            if 0 <= score <= 100:
                return score

    return None