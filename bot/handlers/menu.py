"""Обработчик главного меню — маршрутизация по разделам."""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from texts.scenarios import SCENARIOS


async def menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    key = query.data  # например: menu_symptoms

    scenario = SCENARIOS.get(key)
    if not scenario:
        await query.edit_message_text("Раздел в разработке.")
        return

    keyboard = [[InlineKeyboardButton(btn["label"], callback_data=btn["data"])] for btn in scenario.get("buttons", [])]
    keyboard.append([InlineKeyboardButton("← Назад", callback_data="menu_back")])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text=scenario["text"],
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )
