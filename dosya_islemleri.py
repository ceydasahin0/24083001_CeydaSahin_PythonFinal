import csv
from finans_modeli import Islem


def csv_kaydet(dosya_adi, gelirler, giderler):
    try:
        fieldnames = ["id", "tutar", "tarih", "aciklama", "tip"]
        with open(dosya_adi, "w", newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for item in gelirler + giderler:
                writer.writerow(item.to_dict())
        print("CSV kaydedildi:", dosya_adi)
    except Exception as e:
        print("CSV kaydederken hata:", e)


def csv_oku(dosya_adi):
    gelirler = []
    giderler = []
    try:
        with open(dosya_adi, "r", encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                tip = row.get("tip", "")
                obj = Islem.from_dict(row)
                if tip == "gelir":
                    gelirler.append(obj)
                else:
                    giderler.append(obj)
        print("CSV okundu:", dosya_adi)
    except FileNotFoundError:
        print("CSV dosyası bulunamadı, yeni liste oluşturuluyor.")
    except Exception as e:
        print("CSV okurken hata:", e)
    return gelirler, giderler
