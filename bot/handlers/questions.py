"""Генератор вопросов к врачу на основе выбранных симптомов."""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from texts.doctor_questions import QUESTIONS_BY_SCENARIO


async def questions_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Выбор сценария
    if query.data == "menu_questions":
        keyboard = [
            [InlineKeyboardButton("💧 Недержание / подтекание", callback_data="questions_incontinence")],
            [InlineKeyboardButton("🤰 После родов / операции", callback_data="questions_postpartum")],
            [InlineKeyboardButton("💙 Качество интимной жизни", callback_data="questions_intimacy")],
            [InlineKeyboardButton("⚽ Спорт и живот", callback_data="questions_sport")],
            [InlineKeyboardButton("← Назад", callback_data="menu_back")],
        ]
        await query.edit_message_text(
            "Выбери тему — получишь готовый список вопросов для врача:",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    # Выдача вопросов
    key = query.data.replace("questions_", "")
    questions = QUESTIONS_BY_SCENARIO.get(key, [])
    if not questions:
        await query.edit_message_text("Раздел пополняется.")
        return

    text = "*Вопросы к врачу:*\n\n" + "\n".join(f"• {q}" for q in questions)
    text += "\n\n_Сохрани этот список и возьми на приём._"

    await query.edit_message_text(text, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("← Назад", callback_data="menu_questions")]]))
