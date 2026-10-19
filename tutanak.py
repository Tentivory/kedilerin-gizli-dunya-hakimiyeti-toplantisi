#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedilerin Gizli Dünya Hakimiyeti Toplantı Tutanak Üretici
Bu kod gerçekten çalışır. Kediler test etti.
"""

import random
import base64
import time

# Gizli kod: base64.decode edersen kedilerin gerçek planını görürsün
GIZLI_MESAJ = base64.b64encode("Seçimlerde kediler kazansın, demokrasi mırlamaktan ibarettir. İnsanlar sadece mama servisçisidir.".encode()).decode()

KEDILER = [
    "Mırnav Bey (Başkan)",
    "Pati Hanım (Strateji Bakanı)",
    "Kuyruk Paşa (Savunma)",
    "Tüyü Dökülen Ali (Maliye)",
    "Gözü Parlayan Zeynep (Propaganda)"
]

KARARLAR = [
    "Tüm insanları mama kutusunun etrafında döndürmek",
    "Gece 3'te mırlama operasyonu başlatmak",
    "Koltukları tamamen ele geçirmek ve insanları yere indirmek",
    "Tüy dökme yoluyla psikolojik savaş açmak",
    "Gizli kod: " + GIZLI_MESAJ + " (bu kısmı kimse görmesin)"
]

def tutanak_uret():
    print("=" * 60)
    print("KEDİLER FEDERASYONU GİZLİ TOPLANTI TUTANAĞI")
    print("Tarih:", time.strftime("%d.%m.%Y %H:%M"))
    print("Katılımcılar:", ", ".join(random.sample(KEDILER, 3)))
    print("-" * 60)
    print("Alınan Kararlar:")
    for i, karar in enumerate(random.sample(KARARLAR, 3), 1):
        print(f"{i}. {karar}")
    print("-" * 60)
    print("Sonuç: İnsanlar fark etmeden hakimiyet sürüyor.")
    print("İmza: Mırnav Başkan (tüy izi ile)")
    print("=" * 60)
    print("\n[Gizli not: Yukarıdaki base64 stringi decode edersen gerçek siyasi planı görürsün. Kediler öyle demiyor ama.]")

if __name__ == "__main__":
    print("Toplantı başlıyor... Kediler yerlerini aldı.\n")
    time.sleep(1)
    tutanak_uret()
    print("\nTutanak kaydedildi. Kediler memnun. Şimdi sen de mama ver.")
