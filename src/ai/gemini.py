import json
import os

from google import genai

from .system_prompt import SYSTEM_PROMPT


def _get_client() -> genai.Client:
    """Create a Gemini client using an API key."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable is not set. "
            "Get your key at https://aistudio.google.com/apikey"
        )
    return genai.Client(api_key=api_key)


async def generate_explanation(data: dict) -> str:
    """Generate an executive explanation of the health report using Gemini."""
    client = _get_client()

    prompt = f"""{SYSTEM_PROMPT}

Project Data:
{json.dumps(data, indent=2, default=str)}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
