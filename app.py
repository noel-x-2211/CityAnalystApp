import streamlit as st
import datetime

# --- TERMINAL CONFIG ---
st.set_page_config(page_title="Data Analyst Terminal", layout="wide")

# --- PROFESSIONAL MATRIX THEME ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(#00FF41 0.5px, transparent 0.5px);
        background-size: 30px 30px;
        color: #00FF41 !important;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3, p, span, label { color: #00FF41 !important; text-shadow: 0 0 5px #00FF41; }
    .stButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        width: 100%;
    }
    .stSuccess { background-color: #001a00 !important; color: #00FF41 !important; border: 1px solid #00FF41; }
    </style>
""", unsafe_allow_html=True)

# --- APP HEADER ---
st.title("📟 ANALYST BOOTCAMP: PHASE 1")

# --- DATE LOGIC ---
target_start = datetime.date(2026, 6, 1)
today = datetime.date.today()
days_left = (target_start - today).days

# --- SIDEBAR: MISSION CONTROL ---
st.sidebar.header("📊 SYSTEM STATUS")
if days_left > 0:
    st.sidebar.warning(f"T-MINUS {days_left} DAYS TO LAUNCH")
else:
    st.sidebar.success("MISSION ACTIVE")

st.sidebar.markdown("---")
st.sidebar.write("**Exam Targets:**")
st.sidebar.code("• IITM BS Qualifier\n• CUET Physics/Chem\n• Stats Mastery")

# --- QUESTIONS ENGINE (LOCKED TO JUNE 1ST) ---
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
    except:
        pass
    return tasks_dict

data_engine = load_data()

# FORCING THE DATE TO JUNE 1ST REGARDLESS OF TODAY
start_date_key = "2026-06-01"

st.subheader(f"📅 SCHEDULED START: {start_date_key}")

if start_date_key in data_engine:
    st.info("System Ready. June 1st Curriculum Loaded Below.")
    for i, task in enumerate(data_engine[start_date_key]):
        with st.container():
            st.markdown(f"### ⚡ TASK_{i+1}")
            st.write(task['q'])
            if st.button(f"VERIFY SOLUTION {i+1}"):
                st.success(f"ANALYSIS: {task['a']}")
            st.markdown("---")
else:
    st.error(f"ENTRY NOT FOUND: Please ensure 'questions.txt' has a '{start_date_key}' entry.")

# --- PRE-SEASON PREP ---
with st.expander("📝 PRE-SEASON SYLLABUS CHECK"):
    st.write("**IIT Madras:** Prepare for Computational Thinking and Discrete Math.")
    st.write("**CUET:** Revise NCERT Class 12 Physics (Electrostatics/Current Electricity).")
    st.write("**Career:** Finalize your Python environment setup.")
