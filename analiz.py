import pandas as pd
import numpy as np


def verileri_dataframe_yap(gelirler, giderler):
    rows = []
    for it in gelirler + giderler:
        rows.append(it.to_dict())
    df = pd.DataFrame(rows)
    if not df.empty:
        df["tutar"] = df["tutar"].astype(float)
        df["tarih"] = pd.to_datetime(df["tarih"], errors='coerce')
    return df


def toplam_gelir_gider(df):
    if df.empty:
        return 0.0, 0.0
    toplam_gelir = df.loc[df["tip"] == "gelir", "tutar"].sum()
    toplam_gider = df.loc[df["tip"] == "gider", "tutar"].sum()
    return float(toplam_gelir), float(toplam_gider)


def aylik_analiz(df):
    if df.empty:
        return pd.DataFrame()
    df2 = df.copy()
    df2["yil_ay"] = df2["tarih"].dt.to_period('M')
    summary = df2.groupby(["yil_ay", "tip"])['tutar'].sum().unstack(fill_value=0)
    return summary


def numpy_istatistik(df):
    if df.empty:
        return {}
    tutarlar = df["tutar"].to_numpy()
    return {
        "ortalama": float(np.mean(tutarlar)),
        "min": float(np.min(tutarlar)),
        "max": float(np.max(tutarlar)),
        "std": float(np.std(tutarlar, ddof=0)),
    }
