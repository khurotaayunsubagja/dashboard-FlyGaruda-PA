import streamlit as st
import pandas as pd
import plotly.express as px 

df = pd.read_excel("data-report-dashboard.xlsx")
st.sidebar.header("Filter Data")

# Fitur Filter
selected_sentiment = st.sidebar.multiselect("Pilih Sentimen", options=df["sentiment_label"].unique(),default=df["sentiment_label"].unique())
selected_topic = st.sidebar.multiselect("Pilih Topik",options=df["Topic_Dominant"].unique(),default=df["Topic_Dominant"].unique())

df_filtered = df[(df["sentiment_label"].isin(selected_sentiment)) & (df["Topic_Dominant"].isin(selected_topic))]
st.header("📖 Deskripsi Dataset")

st.write("""
Dataset yang digunakan merupakan ulasan pengguna aplikasi FlyGaruda yang diperoleh dari Google Play Store.

Data telah melalui tahapan preprocessing teks dan kemudian dilakukan klasifikasi sentimen menggunakan model Bi-LSTM serta pemodelan topik menggunakan metode LDA.
""")
tanggal_awal = df_filtered["at"].min().date()
tanggal_akhir = df_filtered["at"].max().date()

st.metric(
    "Periode Data",
    f"{tanggal_awal} s/d {tanggal_akhir}"
)

# Perhitungannya
total_review = len(df_filtered)

topic2_count = len(df_filtered[df_filtered['Topic_Dominant'] == 'Fitur Login dan Akses Akun'])
topic1_count = len(df_filtered[df_filtered['Topic_Dominant'] == 'Layanan Penggunaan Maskapai Garuda Indonesia'])

topic_count = (df_filtered["Topic_Dominant"].value_counts().reset_index())
topic_count.columns = ["Topic_Dominant", "Count"]
dominant_topic = topic_count.iloc[0]["Topic_Dominant"]

topic2_pct = round(topic2_count/total_review*100, 2)
topic1_pct = round(topic1_count/total_review*100, 2)
positive_count = len(df_filtered[df_filtered['sentiment_label'] == 'Positive'])
negative_count = len(df_filtered[df_filtered['sentiment_label'] == 'Negative'])
neutral_count = len(df_filtered[df_filtered['sentiment_label'] == 'Neutral'])

positive_pct = round(positive_count/total_review*100, 2)
negative_pct = round(negative_count/total_review*100, 2)
neutral_pct = round(neutral_count/total_review*100, 2)


sentiment_count = (df_filtered["sentiment_label"].value_counts().reset_index())
sentiment_count.columns = ["Sentiment", "Count"]
dominant_sentiment = sentiment_count.iloc[0]["Sentiment"]


st.header("📊 Pemodelan Topik dengan LDA")
st.subheader("Evaluasi Model LDA dengan Nilai Koherensi")

coherence_df = pd.DataFrame({
    "Jumlah_Topik": [2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Coherence_Score": [0.480, 0.449, 0.460, 0.435, 0.436, 0.437, 0.430, 0.417, 0.414],
})

fig_coherence = px.line(
    coherence_df,
    x="Jumlah_Topik",
    y="Coherence_Score",
    markers=True,
    text="Coherence_Score"
)

fig_coherence.update_traces(
    texttemplate="<b>%{y:.3f}</b>",
    textposition="top center"
)

st.plotly_chart(
    fig_coherence,
    use_container_width=True
)


st.info("""
Grafik menunjukkan nilai koherensi tertinggi terdapat pada pembentukkan 2 topik.
Sehingga, akan diambil 2 topik yang paling sering dibahas pada ulasan pengguna aplikasi FlyGaruda.
""")

topic_keywords = {
    "Penggunaan Layanan Garuda Indonesia":
        "tiket, penerbangan, pembayaran, booking, check-in",

    "Aksesibilitas dan Login Aplikasi":
        "login, otp, password, akun, garudamiles"
}

col1, col2 = st.columns(2)

topics = list(topic_keywords.items())

with col1:
    st.markdown(f"**{topics[0][0]}**")
    st.caption(f"Kata Kunci: {topics[0][1]}")

with col2:
    st.markdown(f"**{topics[1][0]}**")
    st.caption(f"Kata Kunci: {topics[1][1]}")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "✈️ Layanan Pengguna Maskapai Garuda Indonesia",
        f"{topic1_count}",
        f"{topic1_pct}%"
    )

with col2:
    st.metric(
        "🔐 Fitur Login dan Akses Akun",
        f"{topic2_count}",
        f"{topic2_pct}%"
    )

topic_sentiment = (
    df_filtered.groupby(
        ["Topic_Dominant"]
    )
    .size()
    .reset_index(name="Count")
)

fig2 = px.bar(
    topic_sentiment,
    x="Topic_Dominant",
    y="Count",
    color = 'Topic_Dominant',
    text="Count"
)

fig2.update_traces(
    textposition="outside"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)

st.success(
    f"Topik yang paling dominan adalah **{dominant_topic}**."
)
st.info("""
Grafik menunjukkan distribusi topik pengguna terhadap aplikasi FlyGaruda.
Dominasi topik adalah perihal Fitur Login dan Akses Akun. Hal ini mengindikasikan terdapat sesuatu pada fitur Login dan Akses Akun pada aplikasi FlygGaruda.
""")


# ------------ BATAS BATAS BATAS -----------------------
st.header("📊 Analisis Sentimen dengan Bi-LSTM")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Accuracy", "90.15%")
    st.caption("Overall accuracy")

with col2:
    st.metric("Precision", "92.00%")

with col3:
    st.metric("Recall", "90.00%")

with col4:
    st.metric("F1-Score", "91.00%")

accuracy_df = pd.DataFrame({
    "Epoch": [1, 2, 3, 4, 5, 6],
    "Training Accuracy": [0.63, 0.81, 0.92, 0.96, 0.98, 0.99],
    "Validation Accuracy": [0.54, 0.80, 0.90, 0.89, 0.89, 0.91]
})

fig = px.line(
    accuracy_df,
    x="Epoch",
    y=["Training Accuracy", "Validation Accuracy"],
    markers=True,
    title="Training dan Validation Accuracy"
)

fig.update_layout(
    xaxis_title="Epoch",
    yaxis_title="Accuracy",
    legend_title=""
)

st.plotly_chart(fig, use_container_width=True)

st.info(
    "Peningkatan nilai training accuracy dan validation accuracy pada setiap epoch menunjukkan bahwa model Bi-LSTM berhasil mempelajari pola sentimen dengan baik. Validation accuracy sebesar 91% mengindikasikan performa klasifikasi yang tinggi."
)
# ------------ BATAS BATAS BATAS -----------------------
st.header("📊 Sentimen Berdasarkan Topik")

topic_sentiment = (
    df_filtered.groupby(
        ["Topic_Dominant", 'sentiment_label']
    )
    .size()
    .reset_index(name="Count")
)

fig = px.bar(
    topic_sentiment,
    x="Topic_Dominant",
    y="Count",
    color='sentiment_label',
    barmode="group"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.success(
    f"Sentimen yang paling dominan adalah {dominant_sentiment}."
)

st.info("""
Grafik menunjukkan distribusi sentimen pengguna terhadap aplikasi FlyGaruda.
Dominasi sentimen negatif mengindikasikan pengguna cenderung belum puas terhadap layanan aplikasi, sehingga menunjukkan adanya aspek yang masih perlu diperbaiki.
""")

st.header("💬 Contoh Ulasan")

sentiment_choice = st.selectbox(
    "Pilih Sentimen",
    ["positive", "neutral", "negative"]
)

sample = df_filtered[
    df_filtered['sentiment_label'] == sentiment_choice
]

st.dataframe(
    sample[["content"]].sample(7)
)

