# Proyek Analisis Sentimen Karhutla Kalimantan 2026

## 1. Deskripsi Proyek

Proyek ini bertujuan untuk melakukan analisis sentimen dan pemetaan isu terkait peristiwa Kebakaran Hutan dan Lahan (Karhutla) di wilayah Kalimantan pada periode Oktober 2026. Data dihimpun dari perbincangan publik dan pemberitaan di platform X (Twitter) untuk memberikan gambaran komprehensif mengenai respons publik, dampak kesehatan/sosial, serta efektivitas penanggulangan oleh pemerintah dan pihak terkait.

## 2. Gambaran Umum Dataset

* **Format Data**: JSON (`dataset_karhutla_kalimantan.json`)

* **Sumber Data**: Platform X (Twitter)

* **Periode Pengambilan**: Oktober 2026

* **Jumlah Objek/Tweet**: 20 Rekaman Data (Sampel Terverifikasi)

* **Cakupan Isu**:

  * Operasi Modifikasi Cuaca (OMC) & Penaburan Garam (TNI/BNPB).

  * Krisis Kesehatan & Lonjakan Kasus ISPA (>72.000 kasus).

  * Penanggulangan Sosial & Posko Bantuan (Rumah Oksigen Gratis).

  * Dampak Pendidikan (Usulan Penundaan TKA 2026).

  * Ekologi & Lingkungan (Pergerakan Asap ke Selatan/Australia, Satwa Terdampak).

## 3. Struktur Direktori Repositori

```
.
├── README.md                           # Dokumentasi utama proyek
├── data/
│   ├── raw/
│   │   └── dataset_karhutla_kalimantan.json   # Dataset mentah format JSON
│   └── processed/                      # Data hasil pembersihan & ekstraksi (ditambahkan berbertahap)
├── notebooks/                          # Jupyter Notebook untuk eksplorasi
│   ├── 01_data_cleaning_eda.ipynb      # Tahap 1: Cleansing & Exploratory Data Analysis
│   ├── 02_sentiment_analysis.ipynb     # Tahap 2: Labelling & Model Sentiment Analysis
│   └── 03_topic_modeling.ipynb         # Tahap 3: Pemodelan Topik / Klastering Isu
├── src/                                # Source code modul Python
│   ├── __init__.py
│   ├── preprocessing.py                # Fungsi pembersihan teks & penataan JSON
│   └── sentiment.py                    # Klasifikasi sentimen & ekstraksi fitur
├── outputs/                            # Grafik, visualisasi, dan hasil laporan akhir
│   ├── figures/
│   └── reports/
└── requirements.txt                    # Dependensi pustaka Python

```

## 4. Prosedur & Tahapan Kerja (Workflow)

Untuk memastikan pengolahan data berjalan secara sistematis, analisis ini dibagi menjadi 5 tahapan utama:

1. **Tahap 1: Inisialisasi & Data Setup (Saat Ini)**

   * Menata repositori dan membuat dokumentasi standar (`README.md`).

   * Penempatan dataset JSON mentah pada folder `data/raw/`.

2. **Tahap 2: Preprocessing & Exploratory Data Analysis (EDA)**

   * Parsing JSON ke Dataframe (Pandas).

   * *Text Cleansing* (menghapus URL, hashtag, mention, emoji, dan karakter khusus).

   * Normalisasi kata slang/singkatan.

   * Analisis frekuensi kata dan sebaran data dasar.

3. **Tahap 3: Klasifikasi Sentimen (Sentiment Labeling & Analysis)**

   * Pelabelan sentimen (Positif, Netral, Negatif).

   * Analisis proporsi sentimen terhadap berbagai topik (Kesehatan, OMC, Pendidikan).

4. **Tahap 4: Topic Modeling & Klastering Isu**

   * Mengelompokkan isu-isu utama menggunakan metode NLP (misal: LDA / Keyword Extraction).

   * Menghubungkan sentimen publik dengan topik spesifik (misal: Sentimen terhadap penanganan ISPA vs OMC).

5. **Tahap 5: Pelaporan & Visualisasi Hasil**

   * Pembuatan grafik visualisasi (Distribution chart, Word Cloud, Sentiment by Topic).

   * Penyusunan ringkasan eksekutif (*Executive Summary*) untuk rekomendasi penanganan isu.

## 5. Cara Penggunaan (Setup Environment)

```
# 1. Clone repositori ini
git clone https://github.com/username/karhutla-kalimantan-sentiment.git
cd karhutla-kalimantan-sentiment

# 2. Buat virtual environment (Opsional tetapi disarankan)
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
# venv\Scripts\activate   # Untuk Windows

# 3. Install dependensi
pip install -r requirements.txt

```

*Dokumentasi ini akan diperbarui secara berkala sesuai dengan progres pengerjaan proyek.*