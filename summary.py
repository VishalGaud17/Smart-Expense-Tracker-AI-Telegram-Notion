import requests 
import os 
NOTION_TOKEN = os.getenv("NOTION_TOKEN") 
DATABASE_ID = os.getenv("DATABASE_ID") 
headers = { 
    "Authorization": f"Bearer {NOTION_TOKEN}", 
    "Notion-Version": "2022-06-28", "Content-Type": "application/json" 
    } 

def get_monthly_summary(): 
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query" 

    response = requests.post(url, headers=headers)

    results = response.json()["results"] 

    summary = {} 

    for item in results: 
        category = item["properties"]["Category"]["select"]["name"] 
        amount = item["properties"]["Amount"]["number"] 
        summary[category] = summary.get(category, 0) + amount