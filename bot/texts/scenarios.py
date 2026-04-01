"""Сценарии главного меню с текстами и кнопками."""
SCENARIOS = {
    "menu_symptoms": {
        "text": "*Симптомы — выбери то, что подходит:*",
        "buttons": [
            {"label": "💧 Подтекание / недержание", "data": "symptom_incontinence"},
            {"label": "⬇️ Ощущение тяжести / давления", "data": "symptom_heaviness"},
            {"label": "😶 Не чувствую мышцы", "data": "symptom_nofeeling"},
            {"label": "😣 Болевые ощущения в тазу", "data": "symptom_pain"},
            {"label": "💬 Описать своими словами", "data": "symptom_freetext"},
        ],
    },
    "menu_postpartum": {
        "text": "*После родов или операции:*\n\nВыбери что тебя интересует:",
        "buttons": [
            {"label": "🔄 Восстановление тазового дна", "data": "symptom_recovery"},
            {"label": "💧 Недержание после родов", "data": "symptom_postpartum_inc"},
            {"label": "📋 Вопросы к врачу после родов", "data": "questions_postpartum"},
        ],
    },
    "menu_prevention": {
        "text": "*Профилактика и осознанность:*\n\nЭто для тех, у кого нет острых симптомов, но хочется быть в контакте с телом:",
        "buttons": [
            {"label": "🗓 Запустить трекер привычки", "data": "habit_start"},
            {"label": "🌬 Дыхательные практики", "data": "habit_breathing"},
            {"label": "📄 Получить PDF-памятку", "data": "pdf_send"},
        ],
    },
    "menu_ai_symptom": {
        "text": "💬 Напиши своими словами что тебя беспокоит — я разберу.",
        "buttons": [],
    },
}
