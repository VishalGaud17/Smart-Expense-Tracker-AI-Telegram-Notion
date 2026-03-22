import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ---

from datetime import datetime
import pytz

def get_ist_date():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist).strftime("%Y-%m-%d")



def parse_with_ai(text):

    today_ist = get_ist_date()

    prompt = f"""
Extract expenses from the text.

STRICT RULES:
- Return ONLY valid JSON
- Always return a LIST of objects
- Do NOT return empty or dummy values

Each object MUST contain:
- product (real item name, NOT "Unknown")
- amount (number, NOT 0 unless explicitly stated)
- category (choose closest match)
- desc ("" if none)
- date (YYYY-MM-DD or null)

Examples:

Input: "pizza 200"
Output:
[
  {{
    "product": "Pizza",
    "amount": 200,
    "category": "Food",
    "desc": "",
    "date": null
  }}
]

Text: {text}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    result = response.choices[0].message.content

    try:
        data = json.loads(result)
        return data if isinstance(data, list) else [data]
    except:
        print("Raw output:", result)
        return []
