import streamlit as st
import datetime
import pandas as pd

# --- TERMINAL CONFIG ---
st.set_page_config(page_title="Data Analyst Terminal", layout="wide")

# --- CUSTOM CSS: MATRIX / PRO ANALYST THEME ---
st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(#00FF41 0.5px, transparent 0.5px);
        background-size: 30px 30px;
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace;
    }
    
    /* Headers and Text */
    h1, h2, h3, p, span, label {
        color: #00FF41 !important;
        text-shadow: 0 0 5px #00FF41;
    }

    /* Professional Container Styling */
    .stAlert {
        background-color: rgba(0, 255, 65, 0.05) !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
    }

    /* Button Styling */
    .stButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        border-radius: 0px !important;
        width: 100%;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00FF41 !important;
        color: #000000 !important;
    }

    /* Expander Styling */
    .streamlit-expanderHeader {
        background-color: #000000 !important;
        border: 1px solid #00FF41 !important;
        color: #00FF41 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("📟 DATA ANALYST CAREER TERMINAL")
st.markdown("---")

# --- SIDEBAR: CAREER TRACKER ---
st.sidebar.header("🚀 CAREER PROGRESS")
progress = st.sidebar.slider("Syllabus Completion %", 0, 100, 15)
st.sidebar.write(f"**Target:** 20 LPA Data Analyst Role")
st.sidebar.markdown("---")
st.sidebar.write("**Focus Areas:**")
st.sidebar.code("1. IITM BS Degree\n2. CUET Preparation\n3. Python & Stats")

# --- CORE LOGIC: QUESTIONS ENGINE ---
def load_data():
    tasks_dict = {}
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                if "|" in line:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        date_str, question, answer = parts
                        if date_str not in tasks_dict:
                            tasks_dict[date_str] = []
                        tasks_dict[date_str].append({"q": question, "a": answer})
    except FileNotFoundError:
        st.error("SYSTEM ERROR: 'questions.txt' not found in root directory.")
    return tasks_dict

# Initialize Data
data_engine = load_data()
today = datetime.date.today().strftime("%Y-%m-%d")

# --- MAIN DISPLAY ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"📅 Daily Mission: {today}")
    
    # If today's questions exist, show them. Otherwise, show a placeholder for June 1st.
    display_date = today if today in data_engine else "2026-06-01"
    
    if display_date in data_engine:
        for i, task in enumerate(data_engine[display_date]):
            with st.container():
                st.markdown(f"### TASK_{i+1}")
                st.write(task['q'])
                with st.expander("REVEAL ANALYTICAL SOLUTION"):
                    st.success(task['a'])
                st.markdown("<br>", unsafe_allow_html=True)
    else:
        st.info("SYSTEM IDLE: No tasks synced for today. Waiting for 'questions.txt' update.")

with col2:
    st.subheader("📊 Exam Insights")
    with st.expander("IIT Madras BS"):
        st.write("- Focus on Computational Thinking")
        st.write("- Statistics and Probability")
    with st.expander("CUET 2026"):
        st.write("- NCERT Physics/Chemistry")
        st.write("- Logical Reasoning")

# --- FOOTER ---
st.markdown("---")
st.caption("Terminal Status: Online | Encryption: Active | Career Path: 20 LPA Secured")
