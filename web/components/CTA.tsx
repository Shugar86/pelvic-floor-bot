export default function CTA() {
  return (
    <section className="px-6 py-20 bg-[#21D4B0] text-center">
      <div className="mx-auto max-w-xl">
        <h2 className="text-3xl font-bold text-white mb-4">Попробуй прямо сейчас</h2>
        <p className="text-white/80 mb-8">Анонимно. Бесплатно. Без регистрации.</p>
        <a
          href={process.env.NEXT_PUBLIC_BOT_URL || 'https://t.me/your_bot'}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-block rounded-xl bg-white px-8 py-4 text-[#21D4B0] font-semibold text-lg hover:bg-[#F5F4F6] transition-colors"
        >
          Открыть в Telegram →
        </a>
      </div>
    </section>
  )
}
