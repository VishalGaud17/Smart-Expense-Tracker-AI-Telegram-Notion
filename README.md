# 📊 AI Expense Tracker Bot (Telegram + Notion)

> Log daily expenses in plain English via Telegram. AI extracts the data, Notion stores it.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-10A37F?style=flat&logo=openai&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=flat&logo=telegram&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-API-000000?style=flat&logo=notion&logoColor=white)

---

## 💡 What It Does

Type something like `Pizza 300 with friends yesterday` in Telegram — the bot uses OpenAI to parse it, categorize it, detect the date, and save it to your Notion database. That's it.

---

## 🚀 Features

| Feature | Description |
|---|---|
| 💬 Natural Language Input | `Uber 150 from office` — no forms, no dropdowns |
| 🤖 AI Parsing | GPT-4o-mini extracts item, amount, category & date |
| 🗂️ Auto-Categorization | Food, Travel, Entertainment, Shopping, and more |
| 📅 Smart Dates | Understands "today", "yesterday", "last Monday" |
| 🧾 Notion Storage | Expenses saved directly to your Notion database |
| 📊 Monthly Summary | `/summary` command for a full spending breakdown |
| ⚡ Batch Logging | Log multiple expenses in a single message |

---

## 🏗️ Architecture
```
User (Telegram)
      ↓
Telegram Bot (bot.py)
      ↓
OpenAI API → Structured JSON (ai_parser.py)
      ↓
Notion API → Database Storage (notion_utils.py)
      ↓
Summary Engine (summary.py)
```

---

## 📂 Project Structure
```
ai-expense-tracker/
├── ai_parser.py       # AI-based expense extraction (OpenAI)
├── notion_utils.py    # Notion API integration & database writes
├── summary.py         # Monthly summary logic & aggregation
├── bot.py             # Telegram bot handler & command routing
├── .env               # Environment variables (never commit!)
└── requirements.txt   # Python dependencies
```

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-expense-tracker.git
cd ai-expense-tracker
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_TOKEN=your_telegram_bot_token_here
NOTION_TOKEN=your_notion_integration_token_here
DATABASE_ID=your_notion_database_id_here
```

> ⚠️ Add `.env` to your `.gitignore` — never push API keys to GitHub.

### 5. Run the bot
```bash
python bot.py
```

---

## 📊 Notion Database Schema

Set up your Notion database with these exact properties:

| Property | Type | Description |
|---|---|---|
| Product | Title | Name of the expense item |
| Amount | Number | Cost in INR or local currency |
| Category | Select | Food, Travel, Entertainment, etc. |
| Desc | Rich Text | Additional notes or context |
| Date | Date | Date of the expense |

---

## 🧠 Example Inputs
```
Lunch 200
Uber 150 from office
Movie ticket 300 yesterday
Pizza 500 Dominos with friends
Groceries 800 BigBazaar last Monday
```

---

## 📈 Example Output (Notion)

| Product | Amount | Category | Desc | Date |
|---|---|---|---|---|
| Pizza | ₹500 | Food | Dominos with friends | 2026-03-30 |
| Uber | ₹150 | Travel | From office | 2026-03-31 |
| Movie Ticket | ₹300 | Entertainment | — | 2026-03-29 |

---

## 📋 Commands

| Command | Description |
|---|---|
| `/start` | Initialize the bot and see welcome message |
| `/summary` | Get monthly expense breakdown by category |
| `<expense text>` | Log an expense in natural language |

---

## 🧪 Challenges Solved

- Natural language → structured JSON using prompt engineering
- Handling inconsistent and abbreviated user inputs
- Multi-API integration: Telegram + OpenAI + Notion
- Robust error handling for unpredictable LLM outputs
- Smart date resolution for relative terms like "yesterday"

---

## 🔥 Future Improvements

- [ ] 📊 Power BI / Streamlit dashboard
- [ ] 🎙️ Voice input via Telegram voice messages
- [ ] 💬 WhatsApp integration
- [ ] 📈 Spending trends & anomaly detection
- [ ] 🧠 AI-based budgeting suggestions
- [ ] 🔔 Weekly spending alerts & threshold notifications

---

## 👨‍💻 Author

**Vishal Gaud** — Data Analyst | Data Scientist | ML Enthusiast

---

⭐ If you find this useful, give it a star on GitHub!
