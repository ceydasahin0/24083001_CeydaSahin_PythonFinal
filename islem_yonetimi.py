from finans_modeli import Islem
from utils import yeni_id_olustur, tarih_kontrol, sayi_kontrol


def gelir_ekle(gelirler, giderler):
    """Kullanıcıdan gelir bilgisi alır, doğrular ve gelir listesine ekler.

    Args:
        gelirler (list): Mevcut gelir `Islem` listesi.
        giderler (list): Mevcut gider `Islem` listesi (ID benzersizliği için kullanılır).
    """
    try:
        tutar = input("Gelir tutarı: ")
        if not sayi_kontrol(tutar):
            print("Geçersiz tutar")
            return
        tarih = input("Tarih (YYYY-MM-DD): ")
        if not tarih_kontrol(tarih):
            print("Geçersiz tarih formatı")
            return
        aciklama = input("Açıklama: ")
        yeni_id = yeni_id_olustur(gelirler + giderler)
        islem = Islem(id=yeni_id, tutar=float(tutar), tarih=tarih, aciklama=aciklama, tip="gelir")
        gelirler.append(islem)
        print("Gelir eklendi.")
    except Exception as e:
        print("Hata eklerken:", e)


def gider_ekle(gelirler, giderler):
    """Kullanıcıdan gider bilgisi alır, doğrular ve gider listesine ekler.

    Args:
        gelirler (list): Mevcut gelir `Islem` listesi (ID benzersizliği için kullanılır).
        giderler (list): Mevcut gider `Islem` listesi.
    """
    try:
        tutar = input("Gider tutarı: ")
        if not sayi_kontrol(tutar):
            print("Geçersiz tutar")
            return
        tarih = input("Tarih (YYYY-MM-DD): ")
        if not tarih_kontrol(tarih):
            print("Geçersiz tarih formatı")
            return
        aciklama = input("Açıklama: ")
        yeni_id = yeni_id_olustur(gelirler + giderler)
        islem = Islem(id=yeni_id, tutar=float(tutar), tarih=tarih, aciklama=aciklama, tip="gider")
        giderler.append(islem)
        print("Gider eklendi.")
    except Exception as e:
        print("Hata eklerken:", e)


def islemleri_listele(gelirler, giderler):
    print("\n--- Gelirler ---")
    for g in gelirler:
        print(f"ID:{g.id} | {g.tarih} | {g.tutar} | {g.aciklama}")
    print("\n--- Giderler ---")
    for g in giderler:
        print(f"ID:{g.id} | {g.tarih} | {g.tutar} | {g.aciklama}")


def islem_sil(gelirler, giderler, id):
    try:
        id = int(id)
    except Exception:
        print("Geçersiz ID")
        return
    for lst in (gelirler, giderler):
        for i, item in enumerate(lst):
            if int(item.id) == id:
                lst.pop(i)
                print("İşlem silindi.")
                return
    print("ID bulunamadı.")
