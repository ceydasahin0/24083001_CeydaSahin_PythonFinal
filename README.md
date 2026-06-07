# Kişisel Finans ve Harcama Takip Sistemi

Bu proje Python ile kişisel finans takibi için basit, modüler bir uygulama içerir.

Dosyalar:
- `finans_modeli.py`: `Islem` sınıfı
- `utils.py`: Yardımcı kontroller ve `menu_goster`
- `islem_yonetimi.py`: Gelir/gider ekleme, listeleme, silme
- `dosya_islemleri.py`: CSV okuma/yazma
- `analiz.py`: Pandas & NumPy analizleri
- `gorsellestirme.py`: Matplotlib grafik fonksiyonları
- `main.py`: Basit konsol arayüzü

Çalıştırma:

1. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

2. Konsol uygulamasını başlatın:

```bash
python main.py
```

3. Demo (otomatik, interaktif olmayan) çalıştırma ve çıktı üretme:

```bash
python demo.py
```

4. Testler (pytest):

```bash
pip install pytest
pytest -q
```

Teslim için:
- `main.ipynb` veya `.py` dosyalarınız ve `README.md` ile birlikte proje klasörünü `zip`leyin.
- GitHub repo: özel (private) olarak oluşturun, en az 4 commit yapın ve öğretim elemanını collaborator olarak ekleyin.
 
Student: Ceyda Sahin
Student ID: 24083001
Course: BGY210 - Python Programlama II
