import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from finans_modeli import Islem
from dosya_islemleri import csv_kaydet, csv_oku
from analiz import verileri_dataframe_yap, toplam_gelir_gider


def test_csv_roundtrip(tmp_path):
    g = [Islem(id=1, tutar=10.0, tarih="2026-01-01", aciklama="a", tip="gelir")]
    d = [Islem(id=1, tutar=5.0, tarih="2026-01-02", aciklama="b", tip="gider")]
    f = tmp_path / "t.csv"
    csv_kaydet(str(f), g, d)
    gg, dd = csv_oku(str(f))
    assert len(gg) == 1
    assert len(dd) == 1


def test_analysis():
    g = [Islem(id=1, tutar=10.0, tarih="2026-01-01", aciklama="a", tip="gelir")]
    d = [Islem(id=1, tutar=5.0, tarih="2026-01-02", aciklama="b", tip="gider")]
    df = verileri_dataframe_yap(g, d)
    tg, td = toplam_gelir_gider(df)
    assert tg == 10.0
    assert td == 5.0
