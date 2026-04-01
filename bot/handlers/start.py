"""Обработчик /start — приветствие и главное меню."""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from texts.messages import MSG_WELCOME


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🔍 Есть симптомы", callback_data="menu_symptoms")],
        [InlineKeyboardButton("🤰 После родов / операции", callback_data="menu_postpartum")],
        [InlineKeyboardButton("🌱 Хочу профилактику", callback_data="menu_prevention")],
        [InlineKeyboardButton("💬 Разбор симптома с ИИ", callback_data="menu_ai_symptom")],
        [InlineKeyboardButton("📋 Вопросы к врачу", callback_data="menu_questions")],
        [InlineKeyboardButton("📄 Получить PDF-памятку", callback_data="pdf_send")],
        [InlineKeyboardButton("🗓 Трекер привычки (5 мин/день)", callback_data="habit_start")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(MSG_WELCOME, reply_markup=reply_markup, parse_mode="Markdown")
