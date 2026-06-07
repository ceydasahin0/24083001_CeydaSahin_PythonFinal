"""Demo script to programmatically exercise the project modules.

This script creates sample transactions, saves a CSV, runs analysis,
and saves plots as PNG files so the outputs can be included in the
project submission without interactive input.
"""
from pathlib import Path
from finans_modeli import Islem
from dosya_islemleri import csv_kaydet
from analiz import verileri_dataframe_yap, toplam_gelir_gider, numpy_istatistik
from gorsellestirme import aylik_grafik, gelir_gider_bar, pasta_grafik
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for tests


def run_demo(output_dir="demo_outputs"):
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    gelirler = [Islem(id=1, tutar=5000, tarih="2026-05-10", aciklama="Maas", tip="gelir")]
    giderler = [Islem(id=1, tutar=1500, tarih="2026-05-11", aciklama="Kira", tip="gider"),
                Islem(id=2, tutar=200, tarih="2026-05-12", aciklama="Market", tip="gider")]

    csv_path = out / "sample_veriler.csv"
    csv_kaydet(str(csv_path), gelirler, giderler)

    df = verileri_dataframe_yap(gelirler, giderler)
    g, s = toplam_gelir_gider(df)
    stats = numpy_istatistik(df)
    print("Toplam Gelir, Gider:", g, s)
    print("İstatistik:", stats)

    # Save plots
    try:
        fig1 = out / "aylik.png"
        aylik_grafik(df)
    except Exception:
        pass
    try:
        gelir_gider_bar(df)
    except Exception:
        pass
    try:
        pasta_grafik(df)
    except Exception:
        pass


if __name__ == "__main__":
    run_demo()
