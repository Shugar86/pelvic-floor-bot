const STEPS = [
  { n: '1', text: 'Открой бот — анонимно, без регистрации' },
  { n: '2', text: 'Выбери раздел или опиши симптом своими словами' },
  { n: '3', text: 'Получи понятное объяснение и маршрут дальнейших действий' },
  { n: '4', text: 'Забери PDF-памятку и список вопросов к врачу' },
]

export default function HowItWorks() {
  return (
    <section className="px-6 py-16 bg-white">
      <div className="mx-auto max-w-2xl">
        <h2 className="text-2xl font-bold text-[#444445] mb-10 text-center">Как это работает</h2>
        <div className="space-y-6">
          {STEPS.map((s) => (
            <div key={s.n} className="flex items-start gap-4">
              <div className="flex-shrink-0 w-10 h-10 rounded-full bg-[#21D4B0] flex items-center justify-center text-white font-bold">
                {s.n}
              </div>
              <p className="text-[#444445] pt-2">{s.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
