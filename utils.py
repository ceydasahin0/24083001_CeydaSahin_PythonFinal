from datetime import datetime
from typing import List


def yeni_id_olustur(liste: List):
    try:
        if not liste:
            return 1
        max_id = max(int(item.id) for item in liste)
        return max_id + 1
    except Exception:
        return 1


def tarih_kontrol(tarih: str) -> bool:
    try:
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except Exception:
        return False


def sayi_kontrol(deger: str) -> bool:
    try:
        float(deger)
        return True
    except Exception:
        return False


def menu_goster():
    print("\nKişisel Finans - Menü")
    print("1. Gelir Ekle")
    print("2. Gider Ekle")
    print("3. Listele")
    print("4. Analiz Yap")
    print("5. Grafik Göster")
    print("6. CSV Kaydet")
    print("7. CSV Oku")
    print("8. Çıkış")
