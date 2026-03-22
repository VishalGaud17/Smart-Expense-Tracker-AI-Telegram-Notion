from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, filters, ContextTypes

from notion_utils import add_expense
from summary import get_monthly_summary
from ai_parser import parse_with_ai

from dotenv import load_dotenv
import os

load_dotenv()

print("Starting bot...")

TOKEN = os.getenv("TELEGRAM_TOKEN")

from datetime import datetime
import pytz

def get_ist_date():
    ist = pytz.timezone("Asia/Kolkata")
    return datetime.now(ist).strftime("%Y-%m-%d")

def clean_date(date_str):
    ist = pytz.timezone("Asia/Kolkata")

    if not date_str:
        return datetime.now(ist).strftime("%Y-%m-%d")

    try:
        # Handles ISO format (2026-03-20 or with time)
        parsed = datetime.fromisoformat(date_str)
        return parsed.strftime("%Y-%m-%d")
    except:
        try:
            parsed = datetime.strptime(date_str, "%Y-%m-%d")
            return parsed.strftime("%Y-%m-%d")
        except:
            return datetime.now(ist).strftime("%Y-%m-%d")


def is_valid_recent_date(date_str):
    try:
        parsed = datetime.fromisoformat(date_str)
        
        # Accept only dates within last 7 days (adjust if needed)
        today = datetime.now(pytz.timezone("Asia/Kolkata"))
        diff = (today - parsed).days

        return 0 <= diff <= 7
    except:
        return False

# ✅ Handle User Messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        text = update.message.text

        expenses = parse_with_ai(text)

        if not expenses:
            await update.message.reply_text("Couldn't detect any expense ❌")
            return

        for exp in expenses:

            if exp.get("product") in ["Unknown", None] or exp.get("amount", 0) == 0:
                continue

            raw_date = exp.get("date")

            if not raw_date:
                final_date = get_ist_date()
            else:
                final_date = clean_date(raw_date)

            add_expense(
                title=exp.get("product"),
                amount=float(exp.get("amount")),
                category=exp.get("category", "Misc"),
                desc=exp.get("desc", ""),
                date=final_date
            )
        await update.message.reply_text("Expense added ✅")

    except Exception as e:
        print("Error:", e)
        await update.message.reply_text("Something went wrong ❌")



# ✅ Monthly Summary Command
async def summary(update: Update, context: ContextTypes.DEFAULT_TYPE):

    data = get_monthly_summary()

    message = "📊 This Month Spending:\n\n"
    total = 0

    for category, amount in data.items():
        message += f"{category}: ₹{amount}\n"
        total += amount

    message += f"\n💰 Total: ₹{total}"

    await update.message.reply_text(message)


# ✅ Run Bot
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.add_handler(CommandHandler("summary", summary))

app.run_polling()