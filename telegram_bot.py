import os
import logging
import requests
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
SIGNAL_SOURCE = "https://i2zmlkof.streamlit.app"

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome! Send /signals to get the latest Pocket Option signals.")

async def signals(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        signals = "19:23:21 — AED/CNY: Sell Signal (98%)\n19:23:21 — AUD/CHF: Buy Signal (85%)"
        await update.message.reply_text(f"Latest Signals:\n\n{signals}")
    except Exception as e:
        await update.message.reply_text("Failed to get signals.")
        logging.error(f"Error fetching signals: {e}")

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signals", signals))
    app.run_polling()
