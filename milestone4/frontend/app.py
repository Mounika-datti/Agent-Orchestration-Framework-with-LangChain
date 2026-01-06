import streamlit as st
import requests

# ================= CONFIG =================
BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Academic Assistant App",
    page_icon="🎓",
    layout="wide"
)

# ================= STYLES =================
st.markdown("""
<style>
.title {
    font-size: 40px;
    font-weight: 800;
}
.subtitle {
    font-size: 18px;
    color: #6b7280;
    margin-bottom: 20px;
}
.overview {
    background: #eef2ff;
    padding: 18px;
    border-radius: 12px;
    margin-top: 20px;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='title'>🎓 Academic Content Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Search a topic and explore content step by step</div>", unsafe_allow_html=True)

# ================= SESSION STATE =================
if "data" not in st.session_state:
    st.session_state.data = None
if "view" not in st.session_state:
    st.session_state.view = None

# ================= SEARCH =================
topic = st.text_input(
    "🔍 Search Topic",
    placeholder="e.g. Data Structures, DBMS, Operating Systems"
)

if st.button("🚀 Search", use_container_width=True):
    if not topic.strip():
        st.warning("Please enter a topic")
    else:
        with st.spinner("Fetching topic overview..."):
            response = requests.post(
                f"{BACKEND_URL}/generate",
                json={"topic": topic},
                timeout=90
            )

        if response.status_code == 200:
            st.session_state.data = response.json()
            st.session_state.view = None
            st.success("Topic loaded successfully ✅")
        else:
            st.error("Backend error")
            st.code(response.text)

# ================= OVERVIEW + OPTIONS =================
if st.session_state.data:
    data = st.session_state.data

    # ---- OVERVIEW SECTION ----
    st.markdown(
        f"""
        <div class="overview">
        <h3>📌 Topic Overview</h3>
        <p>{data["simplified"][:400]}...</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🔎 Explore More")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📘 Simplified"):
            st.session_state.view = "simple"

    with col2:
        if st.button("📝 Summary"):
            st.session_state.view = "summary"

    with col3:
        if st.button("📂 Notes"):
            st.session_state.view = "notes"

    with col4:
        if st.button("🧠 MCQs"):
            st.session_state.view = "mcqs"

    # ================= CONDITIONAL DISPLAY =================
    if st.session_state.view == "simple":
        st.markdown("<div class='card'><h3>📘 Simplified Explanation</h3></div>", unsafe_allow_html=True)
        st.write(data["simplified"])

    elif st.session_state.view == "summary":
        st.markdown("<div class='card'><h3>📝 Summary Notes</h3></div>", unsafe_allow_html=True)
        st.write(data["summary"])

    elif st.session_state.view == "notes":
        st.markdown("<div class='card'><h3>📂 Formatted Exam Notes</h3></div>", unsafe_allow_html=True)
        st.markdown(data["formatted_notes"])

        if st.button("📄 Download Notes as PDF"):
            pdf_response = requests.post(
                f"{BACKEND_URL}/download-pdf",
                json={"topic": topic}
            )
            with open("notes.pdf", "wb") as f:
                f.write(pdf_response.content)
            st.success("PDF downloaded as notes.pdf")

    elif st.session_state.view == "mcqs":
        st.markdown("<div class='card'><h3>🧠 Practice MCQs</h3></div>", unsafe_allow_html=True)
        st.write(data["mcqs"])

# ================= HISTORY =================
st.markdown("---")
if st.button("📜 View Search History"):
    history = requests.get(f"{BACKEND_URL}/history").json()
    if history:
        st.write(history)
    else:
        st.info("No history available")
