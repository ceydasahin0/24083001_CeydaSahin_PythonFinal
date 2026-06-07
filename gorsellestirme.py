import matplotlib.pyplot as plt


def aylik_grafik(df):
    if df.empty:
        print("Veri yok")
        return
    df2 = df.copy()
    df2['yil_ay'] = df2['tarih'].dt.to_period('M')
    summary = df2.groupby(['yil_ay', 'tip'])['tutar'].sum().unstack(fill_value=0)
    summary.plot(kind='line', marker='o')
    plt.title('Aylık Gelir ve Gider')
    plt.xlabel('Yıl-Ay')
    plt.ylabel('Tutar')
    plt.tight_layout()
    plt.show()


def gelir_gider_bar(df):
    if df.empty:
        print("Veri yok")
        return
    toplam_gelir = df.loc[df['tip'] == 'gelir', 'tutar'].sum()
    toplam_gider = df.loc[df['tip'] == 'gider', 'tutar'].sum()
    plt.bar(['Gelir', 'Gider'], [toplam_gelir, toplam_gider], color=['green', 'red'])
    plt.title('Toplam Gelir vs Gider')
    plt.ylabel('Tutar')
    plt.tight_layout()
    plt.show()


def pasta_grafik(df):
    if df.empty:
        print("Veri yok")
        return
    totals = [df.loc[df['tip'] == 'gelir', 'tutar'].sum(), df.loc[df['tip'] == 'gider', 'tutar'].sum()]
    labels = ['Gelir', 'Gider']
    plt.pie(totals, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
    plt.title('Gelir/Gider Oranları')
    plt.tight_layout()
    plt.show()
