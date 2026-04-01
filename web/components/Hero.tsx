export default function Hero() {
  return (
    <section className="bg-white px-6 py-20 text-center">
      <div className="mx-auto max-w-2xl">
        <span className="inline-block rounded-full bg-[#EEEEF4] px-4 py-1.5 text-sm text-[#A1A1AE] mb-6">
          Бесплатно · Анонимно · Без рекламы
        </span>
        <h1 className="text-4xl font-bold text-[#444445] leading-tight mb-4">
          Тазовое дно —{' '}
          <span className="text-[#21D4B0]">без стыда</span>
        </h1>
        <p className="text-lg text-[#A1A1AE] mb-8">
          Анонимный Telegram-бот и бесплатные материалы по здоровью тазового дна.
          Разберём симптомы, дадим безопасные шаги и поможем понять когда нужен врач.
        </p>
        <a
          href={process.env.NEXT_PUBLIC_BOT_URL || 'https://t.me/your_bot'}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-block rounded-xl bg-[#21D4B0] px-8 py-4 text-white font-semibold text-lg hover:bg-[#22C0A0] transition-colors"
        >
          Открыть бот в Telegram →
        </a>
      </div>
    </section>
  )
}
