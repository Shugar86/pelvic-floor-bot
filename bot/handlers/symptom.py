"""Разбор симптомов — кнопочный сценарий + AI-разбор через OpenRouter."""
import os
from openai import AsyncOpenAI
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from texts.messages import MSG_SYMPTOM_INTRO, MSG_AI_DISCLAIMER

client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)
MODEL = os.getenv("OPENROUTER_MODEL", "google/gemma-3-27b-it:free")

SYSTEM_PROMPT = """Ты — дружелюбный помощник по здоровью тазового дна.
Ты НЕ ставишь диагнозы и НЕ назначаешь лечение.
Ты объясняешь возможные причины симптомов понятным языком,
говоришь когда нужно обратиться к врачу (гинекологу, урологу, реабилитологу),
и даёшь безопасные общие рекомендации (дыхание, расслабление, осанка).
Отвечай на русском языке. Будь кратким (3-5 предложений).
В конце всегда добавляй: 'Это не медицинская консультация. При сомнениях — обратись к врачу.'
"""


async def symptom_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Кнопочный сценарий
    if update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(
            text=MSG_SYMPTOM_INTRO,
            parse_mode="Markdown"
        )
        return

    # Свободный текст → AI-разбор
    user_text = update.message.text
    if not user_text or len(user_text) < 5:
        return

    await update.message.reply_text("🔍 Анализирую... секунду")

    try:
        response = await client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_text},
            ],
            max_tokens=400,
        )
        answer = response.choices[0].message.content
    except Exception as e:
        answer = f"Не удалось получить ответ. Попробуй позже.\n\n_{e}_"

    await update.message.reply_text(
        f"{answer}\n\n{MSG_AI_DISCLAIMER}",
        parse_mode="Markdown"
    )
