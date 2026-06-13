import streamlit as st

st.set_page_config(
    page_title="About Me",
    page_icon="👨‍💻",
    layout="wide"
)

st.title("👨‍💻 About Me")
st.divider()

# =========================
# Header Profile
# =========================
col1, col2 = st.columns([1, 2])

with col1:
    st.image("profile7.png", width=250)

with col2:
    st.markdown("## Khurotaayun Pesona Subagja")

    st.markdown("""
    **Data Enthusiast | Data Analyst | Undergraduate Business Statistics Student**

    I am a final-year Business Statistics student with a strong interest in
    Data Science, Machine Learning, Text Mining, Natural Language Processing (NLP),
    and Data Visualization. I enjoy transforming data into meaningful insights
    to support data-driven decision-making.
    """)

st.divider()

# =========================
# Main Content
# =========================
col_left, col_right = st.columns(2)

# ---------- LEFT ----------
with col_left:

    st.subheader("🎓 Education")

    st.write("""
    **Bachelor of Applied Science in Business Statistics**

    Areas of Interest:
    - Data Science
    - Machine Learning
    - Text Mining
    - Data Analytics
    - Business Intelligence

    **SMAN 5 Bogor**
    """)

    st.markdown("---")

    st.subheader("💼 Experience & Qualifications")

    st.write("""
    - Teaching Assistant for the Database Management course.
    - Developed the East Java Tourism Dashboard 2024.
    - Built a Driver Drowsiness Detection System using YOLO-based computer vision.
    - Experienced in data analysis, dashboard development, and data visualization.
    """)

    st.markdown("---")

    st.subheader("🔬 Research")

    st.write("""
    **_Sentiment Analysis and Topic Modeling of FlyGaruda User Reviews Using Bi-LSTM and LDA_**

    This research focuses on analyzing user sentiment and discovering
    discussion topics from FlyGaruda application reviews using
    Natural Language Processing (NLP) techniques, specifically
    Bidirectional Long Short-Term Memory (Bi-LSTM) and
    Latent Dirichlet Allocation (LDA).
    """)

# ---------- RIGHT ----------
with col_right:

    st.subheader("📚 Tools & Libraries")

    st.write("""
    ### Programming
    - Python
    - SQL
    - VBA

    ### Data Visualization
    - Power BI
    - Tableau
    - Plotly
    - Looker Studio

    ### Machine Learning & NLP
    - TensorFlow
    - Keras
    - Scikit-learn
    - Gensim

    ### Data Processing
    - Pandas
    - NumPy
    """)

    st.markdown("---")

    st.subheader("🛠️ Skills")

    st.write("""
    - 📊 Data Analysis
    - 📈 Data Visualization
    - 🤖 Machine Learning
    - 🧠 Deep Learning
    - 💬 Natural Language Processing
    - 📑 Statistical Analysis
    """)

# =========================
# Contact
# =========================
st.divider()

st.subheader("📞 Contact")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("""
    📧 **Email**
    
    skhurotaayun@gmail.com
    """)

with col2:
    st.write("""
    🔗 **LinkedIn**
    
    linkedin.com/in/khurotaayunpesonasubagja
    """)

with col3:
    st.write("""
    🐙 **GitHub**
    
    github.com/khurotaayunsubagja
    """)