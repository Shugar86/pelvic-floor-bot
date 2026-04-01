"""Компонент PDF-памятки через @react-pdf/renderer.
Запускается отдельно: npx ts-node pdf/generate.ts
"""
import React from 'react'
import { Document, Page, Text, View, StyleSheet } from '@react-pdf/renderer'

const styles = StyleSheet.create({
  page: { backgroundColor: '#FFFFFF', padding: 40, fontFamily: 'Helvetica' },
  header: { backgroundColor: '#21D4B0', padding: 20, borderRadius: 8, marginBottom: 24 },
  headerText: { color: '#FFFFFF', fontSize: 20, fontWeight: 'bold' },
  section: { marginBottom: 20 },
  sectionTitle: { fontSize: 14, fontWeight: 'bold', color: '#444445', marginBottom: 8 },
  item: { fontSize: 11, color: '#444445', marginBottom: 4, paddingLeft: 12 },
  redFlag: { fontSize: 11, color: '#DF3434', marginBottom: 4, paddingLeft: 12 },
  footer: { marginTop: 30, borderTopWidth: 1, borderTopColor: '#EEEEF4', paddingTop: 12 },
  footerText: { fontSize: 9, color: '#A1A1AE', textAlign: 'center' },
})

export const Pamyatka = () => (
  <Document>
    <Page size="A4" style={styles.page}>
      <View style={styles.header}>
        <Text style={styles.headerText}>🌿 Тазовое дно — без стыда</Text>
        <Text style={{ color: 'rgba(255,255,255,0.85)', fontSize: 11, marginTop: 4 }}>
          Памятка по основам здоровья тазового дна
        </Text>
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>🔴 Красные флаги — обратись к врачу</Text>
        {[
          'Боль в области таза, которая не проходит',
          'Кровотечение вне менструального цикла',
          'Ощущение выпадения органов или давления «наружу»',
          'Острое недержание, которое появилось внезапно',
          'Боль при мочеиспускании или половом акте',
        ].map((t, i) => <Text key={i} style={styles.redFlag}>• {t}</Text>)}
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>✅ 3 безопасных базовых шага</Text>
        {[
          '1. Дыхание — диафрагмальное дыхание 5 мин в день расслабляет тазовое дно',
          '2. Осанка — нейтральный таз снижает нагрузку на мышцы тазового дна',
          '3. Осознанность — научись различать напряжение и расслабление мышц',
        ].map((t, i) => <Text key={i} style={styles.item}>{t}</Text>)}
      </View>

      <View style={styles.section}>
        <Text style={styles.sectionTitle}>📋 Вопросы к врачу на первом приёме</Text>
        {[
          '• Какой тип нарушения у меня — гипертонус или гипотонус?',
          '• Безопасно ли мне начинать упражнения?',
          '• Нужна ли диагностика перед тренировками?',
          '• Нужен ли тренажёр с биологической обратной связью?',
          '• К кому ещё стоит обратиться — реабилитолог, уролог?',
        ].map((t, i) => <Text key={i} style={styles.item}>{t}</Text>)}
      </View>

      <View style={styles.footer}>
        <Text style={styles.footerText}>
          Это не медицинская консультация. При любых сомнениях — обратитесь к врачу.
          Благотворительный проект. Без рекламы.
        </Text>
      </View>
    </Page>
  </Document>
)
