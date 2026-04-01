"""Отправка PDF-памятки пользователю."""
from telegram import Update
from telegram.ext import ContextTypes
import os


async def pdf_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    pdf_path = os.path.join(os.path.dirname(__file__), "../../pdf/pamyatka.pdf")

    if not os.path.exists(pdf_path):
        await query.message.reply_text(
            "📄 PDF-памятка скоро будет готова.\n"
            "Пока могу предложить краткую текстовую версию:",
        )
        await query.message.reply_text(
            "*3 безопасных шага для начала:*\n\n"
            "1️⃣ *Дыхание* — диафрагмальное дыхание 5 мин в день расслабляет тазовое дно\n"
            "2️⃣ *Осанка* — нейтральное положение позвоночника снижает нагрузку\n"
            "3️⃣ *Осознанность* — научись различать напряжение и расслабление мышц\n\n"
            "_Это не лечение. При симптомах обратись к врачу._",
            parse_mode="Markdown"
        )
        return

    await query.message.reply_document(
        document=open(pdf_path, "rb"),
        filename="pamyatka_tazovoe_dno.pdf",
        caption="🌿 Памятка по тазовому дну. Сохрани себе."
    )
