import streamlit as st

st.markdown("""
<style>
[data-testid="stSidebarNav"]::before {
    content: "✈️ FlyGaruda Review Dashboard";
    margin-left: 0px;
    margin-bottom: 20px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="Dashboard Sentimen FlyGaruda",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Dashboard Sentimen Ulasan FlyGaruda")
st.write("Selamat datang di dashboard analisis sentimen dan pemodelan topik ulasan pengguna aplikasi FlyGaruda.")