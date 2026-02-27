import os
from openai import OpenAI
from dotenv import load_dotenv
from .prompts import SYSTEM_PROMPT
from .utils import safe_parse_json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_code(code: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": code}
        ],
        temperature=0.2
    )

    content = response.choices[0].message.content
    parsed = safe_parse_json(content)

    if parsed:
        return parsed
    else:
        return {"error": "Failed to parse model output"}