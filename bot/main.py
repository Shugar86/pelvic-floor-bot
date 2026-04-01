"""Точка входа Telegram-бота."""
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
import os

from handlers.start import start_handler
from handlers.menu import menu_handler
from handlers.symptom import symptom_handler
from handlers.habit import habit_handler
from handlers.questions import questions_handler
from handlers.pdf import pdf_handler

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    app = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CallbackQueryHandler(menu_handler, pattern="^menu_"))
    app.add_handler(CallbackQueryHandler(symptom_handler, pattern="^symptom_"))
    app.add_handler(CallbackQueryHandler(habit_handler, pattern="^habit_"))
    app.add_handler(CallbackQueryHandler(questions_handler, pattern="^questions_"))
    app.add_handler(CallbackQueryHandler(pdf_handler, pattern="^pdf_"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, symptom_handler))

    logger.info("Бот запущен")
    app.run_polling()


if __name__ == "__main__":
    main()
