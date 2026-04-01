const FEATURES = [
  { emoji: '🔍', title: 'Разбор симптомов', desc: 'Опиши что беспокоит — бот объяснит возможные причины понятным языком' },
  { emoji: '📋', title: 'Вопросы к врачу', desc: 'Готовый чек-лист вопросов для гинеколога, уролога или реабилитолога' },
  { emoji: '🗓', title: 'Трекер привычки', desc: '7-дневный мягкий план: дыхание, осанка, осознанность — 5 минут в день' },
  { emoji: '📄', title: 'PDF-памятка', desc: 'Красные флаги и 3 безопасных базовых шага — сохрани и поделись' },
]

export default function WhatIs() {
  return (
    <section className="px-6 py-16 bg-[#F5F4F6]">
      <div className="mx-auto max-w-3xl">
        <h2 className="text-2xl font-bold text-[#444445] mb-10 text-center">Что умеет бот</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
          {FEATURES.map((f) => (
            <div key={f.title} className="rounded-2xl bg-white p-6 shadow-sm">
              <div className="text-3xl mb-3">{f.emoji}</div>
              <h3 className="font-semibold text-[#444445] mb-1">{f.title}</h3>
              <p className="text-sm text-[#A1A1AE]">{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
