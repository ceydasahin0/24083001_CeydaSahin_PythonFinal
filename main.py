from finans_modeli import Islem
from islem_yonetimi import gelir_ekle, gider_ekle, islemleri_listele, islem_sil
from dosya_islemleri import csv_kaydet, csv_oku
from analiz import verileri_dataframe_yap, toplam_gelir_gider, aylik_analiz, numpy_istatistik
from gorsellestirme import aylik_grafik, gelir_gider_bar, pasta_grafik
from utils import menu_goster


def main():
    gelirler = []
    giderler = []
    while True:
        menu_goster()
        choice = input("Seçiminiz: ")
        if choice == '1':
            gelir_ekle(gelirler)
        elif choice == '2':
            gider_ekle(giderler)
        elif choice == '3':
            islemleri_listele(gelirler, giderler)
        elif choice == '4':
            df = verileri_dataframe_yap(gelirler, giderler)
            g, s = toplam_gelir_gider(df)
            print(f"Toplam Gelir: {g} | Toplam Gider: {s}")
            print("Numpy istatistik:", numpy_istatistik(df))
            print("Aylık özet:")
            print(aylik_analiz(df))
        elif choice == '5':
            df = verileri_dataframe_yap(gelirler, giderler)
            print("1: Aylık grafik\n2: Gelir-Gider bar\n3: Pasta grafik")
            c = input("Seçim: ")
            if c == '1':
                aylik_grafik(df)
            elif c == '2':
                gelir_gider_bar(df)
            elif c == '3':
                pasta_grafik(df)
        elif choice == '6':
            fname = input("CSV dosya adı (örnek: veriler.csv): ")
            csv_kaydet(fname, gelirler, giderler)
        elif choice == '7':
            fname = input("CSV dosya adı oku (örnek: veriler.csv): ")
            g, d = csv_oku(fname)
            gelirler.extend(g)
            giderler.extend(d)
        elif choice == '8':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim")


if __name__ == '__main__':
    main()
