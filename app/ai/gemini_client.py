import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Correct syntax with quotes around the string:
ENV_PATH = Path(__file__).resolve().parent.parent.parent / ".env"
load_dotenv(dotenv_path=ENV_PATH)

def get_gemini_client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(f"GEMINI_API_KEY not found at {ENV_PATH}")
    return genai.Client(api_key="AQ.Ab8RN6IFhEoYsout2jNj4u9w9f0DY8I7xLCuQ5Eb0Q9Wb6sY0A...")