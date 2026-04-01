"""Трекер привычки — 5-минутный ежедневный ритуал."""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from texts.habit_plan import HABIT_DAYS


async def habit_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Определяем день (хранится в user_data)
    day = context.user_data.get("habit_day", 1)

    if day > len(HABIT_DAYS):
        await query.edit_message_text(
            "🎉 Ты прошла 7-дневный базовый цикл! Отличная работа.\n"
            "Хочешь повторить или перейти к следующему уровню?"
        )
        context.user_data["habit_day"] = 1
        return

    plan = HABIT_DAYS[day - 1]
    text = f"*День {day} из 7*\n\n{plan['title']}\n\n{plan['description']}\n\n⏱ {plan['duration']}"

    keyboard = [
        [InlineKeyboardButton("✅ Сделала — следующий день", callback_data="habit_next")],
        [InlineKeyboardButton("← Главное меню", callback_data="menu_back")],
    ]
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
