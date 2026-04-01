import Hero from '@/components/Hero'
import WhatIs from '@/components/WhatIs'
import HowItWorks from '@/components/HowItWorks'
import Safety from '@/components/Safety'
import CTA from '@/components/CTA'
import Footer from '@/components/Footer'

export default function Home() {
  return (
    <main className="min-h-screen bg-[#F5F4F6]">
      <Hero />
      <WhatIs />
      <HowItWorks />
      <Safety />
      <CTA />
      <Footer />
    </main>
  )
}
