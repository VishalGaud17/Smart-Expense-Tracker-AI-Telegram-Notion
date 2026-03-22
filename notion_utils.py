import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}


def add_expense(title, amount, category, desc, date):

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Product": {
                "title": [{"text": {"content": title}}]
            },
            "Amount": {
                "number": amount
            },
            "Category": {
                "select": {"name": category}
            },
            "Desc": {
                "rich_text": [{"text": {"content": desc}}]
            },
            "Date": {
                "date": {"start": date}
            }
        }
    }

    r = requests.post(
        "https://api.notion.com/v1/pages",
        headers=headers,
        json=data
    )

    print("Notion response:", r.status_code, r.text)