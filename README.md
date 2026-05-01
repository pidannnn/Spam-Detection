# Spam Detection using NLP

Proyek ini merupakan tugas kelompok mata kuliah **Natural Language Processing (NLP)** yang bertujuan membangun sistem **Spam Detection** menggunakan teknik pemrosesan bahasa alami dan machine learning. Sistem ini mampu mengklasifikasikan pesan teks menjadi **Spam** atau **Ham (bukan spam)**.

## 👥 Anggota Kelompok

1. Fi’adn Fawzul Adzhim
2. Noval Putra Siregar
3. Muhamad Ihsan

---

## 📌 Deskripsi Proyek

Spam message merupakan pesan tidak diinginkan yang sering berisi promosi, penipuan, phishing, atau iklan. Pada proyek ini dilakukan pembangunan model klasifikasi teks untuk mendeteksi spam secara otomatis menggunakan tahapan NLP, yaitu:

* Data Collection
* Text Preprocessing
* Feature Extraction
* Modeling
* Evaluation
* Deployment

---

## 🗂️ Struktur Repository

```bash
spam-detection-nlp/
│── dataset/
│   └── spam.csv
│── notebook/
│   └── Spam_Detection.ipynb
│── models/
│   ├── tfidf_vectorizer.pkl
│   ├── naive_bayes.pkl
│   ├── logistic_regression.pkl
│   └── svm.pkl
│── app/
│   └── app.py
│── requirements.txt
│── README.md
```

---

## 📊 Dataset

Dataset yang digunakan berasal dari Kaggle:

* SMS Spam Dataset (>10.000 data)

Sumber dataset:
https://www.kaggle.com/datasets/tinu10kumar/sms-spam-dataset

---

## ⚙️ Tahapan Pengerjaan

### 1. Data Collection

Menggunakan dataset pesan SMS berlabel spam dan ham.

### 2. Text Preprocessing

Tahapan preprocessing yang dilakukan:

* Case Folding
* Tokenization
* Stopword Removal
* Stemming / Lemmatization

### 3. Feature Extraction

Metode yang digunakan:

* TF-IDF
* Word Embedding (Word2Vec)

### 4. Modeling

Model klasifikasi yang digunakan:

* Naive Bayes
* Logistic Regression
* Support Vector Machine (SVM)

### 5. Evaluation Metric

Evaluasi model menggunakan:

* Accuracy
* Precision
* Recall
* F1-Score

---

## 🏆 Hasil Sementara

Contoh hasil evaluasi:

| Model               | Accuracy   | Precision  | Recall | F1-score   |
| ------------------- | ---------- | ---------- | ------ | ---------- |
| Naive Bayes         | 90.97%     | 72.01%     | 95.36% | 82.07%     |
| Logistic Regression | 93.84%     | 95.21%     | 75.36% | 84.13%     |
| SVM                 | **95.35%** | **96.50%** | 81.47% | **88.36%** |

📌 Model terbaik sementara: **SVM**

---

## 🚀 Deployment

Aplikasi sederhana dibuat menggunakan **Gradio**.

Untuk menjalankan:

```bash
pip install -r requirements.txt
python app/app.py
```

Jika menggunakan Google Colab:

```bash
!python app.py
```

Atau akses link ini (Jika belum expired):
https://48745bcccaa8095f55.gradio.live/

---

## 📦 Requirements

Install dependency:

```bash
pip install pandas numpy scikit-learn nltk gensim gradio joblib
```

Atau:

```bash
pip install -r requirements.txt
```

---


## 📈 Kesimpulan

Berdasarkan hasil pengujian, model **Support Vector Machine (SVM)** memberikan performa terbaik pada tugas klasifikasi spam detection dengan kombinasi fitur TF-IDF.

---

## 📌 Catatan

Repository ini dibuat untuk keperluan tugas mata kuliah **Natural Language Processing**.

---

## 📬 Kontak

Jika ada pertanyaan, silakan hubungi anggota kelompok.
