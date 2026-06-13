import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="📌",
    layout="wide"
)

st.title("👋 Selamat Datang di Dashboard Ulasan Aplikasi FlyGaruda")

st.markdown("---")

st.header("Tentang Garuda Indonesia")

st.write("""
Garuda Indonesia merupakan maskapai penerbangan nasional Indonesia yang berdiri sejak tahun 1949.
Sebagai maskapai full-service carrier, Garuda Indonesia melayani berbagai rute domestik dan internasional dengan mengutamakan keselamatan, kenyamanan, dan kualitas pelayanan bagi pelanggan.
""")

st.markdown("---")

st.header("Tentang Aplikasi FlyGaruda")

st.write("""
FlyGaruda adalah aplikasi resmi Garuda Indonesia yang dirancang untuk memberikan kemudahan kepada pelanggan dalam mengakses berbagai layanan penerbangan secara digital.

Melalui aplikasi FlyGaruda, pengguna dapat:

✈️ Memesan tiket penerbangan

📅 Mengelola jadwal penerbangan

🧾 Melakukan check-in online

🎁 Mengakses GarudaMiles

📢 Mendapatkan informasi promo terbaru

Dashboard ini dibangun untuk melakukan analisis sentimen terhadap ulasan pengguna aplikasi FlyGaruda yang tersedia di Google Play Store.
""")

st.markdown("---")

st.header("Tentang Penelitian")

st.write("""
Penelitian ini dilakukan untuk menganalisis opini dan pengalaman pengguna aplikasi FlyGaruda berdasarkan ulasan yang tersedia pada Google Play Store.

Ulasan pengguna merupakan sumber informasi yang penting bagi perusahaan karena berisi berbagai masukan, kritik, keluhan, maupun apresiasi terhadap layanan yang diberikan. Namun, jumlah ulasan yang terus bertambah membuat proses analisis secara manual menjadi kurang efektif.

Oleh karena itu, penelitian ini memanfaatkan teknik Text Mining dan Natural Language Processing (NLP) untuk mengidentifikasi sentimen pengguna serta menemukan topik-topik utama yang sering dibahas dalam ulasan aplikasi.
""")

st.subheader("🎯 Tujuan Penelitian")

st.write("""
- Mengidentifikasi sentimen pengguna aplikasi FlyGaruda ke dalam kategori positif, netral, dan negatif.
- Menganalisis persebaran sentimen pengguna berdasarkan ulasan yang diberikan.
- Menemukan topik-topik utama yang sering muncul dalam ulasan menggunakan metode pemodelan topik.
- Memberikan informasi yang dapat digunakan sebagai bahan evaluasi dan pengembangan layanan aplikasi FlyGaruda.
""")

st.subheader("⚙️ Metode yang Digunakan")

st.write("""
Penelitian ini menggunakan beberapa tahapan analisis data teks, yaitu:

1. Pengumpulan data ulasan pengguna dari Google Play Store.
2. Preprocessing teks yang meliputi cleaning, case folding, tokenizing, normalisasi, stemming, dan stopword removal.
3. Klasifikasi sentimen menggunakan model Bidirectional Long Short-Term Memory (Bi-LSTM).
4. Pemodelan topik menggunakan Latent Dirichlet Allocation (LDA) untuk menemukan topik yang dominan dalam ulasan pengguna.
5. Visualisasi hasil analisis dalam bentuk dashboard interaktif.
""")

st.subheader("📊 Fitur Dashboard")

st.write("""
Dashboard ini menyediakan beberapa fitur utama, yaitu:

🏠 Home
: Menampilkan informasi mengenai Garuda Indonesia, aplikasi FlyGaruda, dan penelitian yang dilakukan.

🤖 Classification Sentiment
: Melakukan prediksi sentimen terhadap teks ulasan yang dimasukkan pengguna menggunakan model Bi-LSTM.

📈 Report Review
: Menampilkan statistik ulasan pengguna, distribusi sentimen, visualisasi data, serta hasil pemodelan topik.

👨‍💻 Creator
: Menampilkan informasi mengenai pengembang dashboard dan penelitian.
""")

st.success("""
Dashboard ini dikembangkan sebagai media visualisasi hasil penelitian analisis sentimen dan pemodelan topik pada ulasan pengguna aplikasi FlyGaruda.
""")