import os
import json
from typing import Optional
from google import genai


def _get_client() -> genai.Client:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return None
    return genai.Client(api_key=api_key)


def sentiment_score(feedback: list = None) -> Optional[float]:
    """
    Analyze stakeholder feedback using Gemini AI to determine sentiment.

    Takes a list of stakeholder feedback strings, sends them to Gemini
    for NLP-based sentiment classification, and returns a score (0-100).

    Scoring:
        Positive  → 100
        Neutral   → 60
        Negative  → 20

    The final score is the average across all feedback entries.
    """
    if not feedback or len(feedback) == 0:
        return None

    client = _get_client()
    if client is None:
        return None

    prompt = f"""Analyze the sentiment of each stakeholder feedback below.
For each feedback, respond with exactly one word: "positive", "neutral", or "negative".
Return the results as a JSON array of strings.

Feedback:
{json.dumps(feedback)}

Example output: ["positive", "neutral", "negative"]
Return ONLY the JSON array, no other text.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]

        sentiments = json.loads(text.strip())

        score_map = {
            "positive": 100,
            "neutral": 60,
            "negative": 20,
        }

        scores = []
        for s in sentiments:
            s_lower = s.strip().lower()
            scores.append(score_map.get(s_lower, 60))

        if not scores:
            return None

        return sum(scores) / len(scores)

    except Exception:
        # Gracefully handle API errors — return None (missing data)
        return None
