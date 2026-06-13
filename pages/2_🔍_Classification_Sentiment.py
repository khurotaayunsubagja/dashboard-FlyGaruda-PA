import streamlit as st
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

@st.cache_resource
def load_artifacts():

    model = load_model("model_bilstm_flygaruda.keras")

    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)

    with open("label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)

    with open("config.pkl", "rb") as f:
        config = pickle.load(f)

    return model, tokenizer, label_encoder, config


model, tokenizer, label_encoder, config = load_artifacts()

max_len = config["max_len"]

st.title("Analisis Sentimen FlyGaruda")

review = st.text_area(
    "Masukkan Ulasan",
    height=150
)

if st.button("Prediksi"):

    if review.strip() == "":
        st.warning("Masukkan ulasan terlebih dahulu")

    else:

        sequence = tokenizer.texts_to_sequences([review])

        padded = pad_sequences(
            sequence,
            maxlen=max_len,
            padding="post",
            truncating="post"
        )

        probability = float(
            model.predict(
                padded,
                verbose=0
            )[0][0]
        )

        pred_class = 1 if probability > 0.5 else 0

        sentiment = label_encoder.inverse_transform(
            [pred_class]
        )[0]

        st.subheader("Hasil")

        st.write(
            f"Sentimen: {sentiment}"
        )

        st.write(
            f"Probabilitas Positif: {probability:.4f}"
        )

        st.write(
            f"Probabilitas Negatif: {1 - probability:.4f}"
        )