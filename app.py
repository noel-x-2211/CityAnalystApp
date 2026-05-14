import streamlit as st
import datetime

# --- SYSTEM CONFIG ---
st.set_page_config(page_title="20 LPA Analyst Terminal", layout="wide")

# --- ADVANCED TERMINAL CSS ---
st.markdown("""
    <style>
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(#00FF41 0.5px, transparent 0.5px);
        background-size: 30px 30px;
        color: #00FF41 !important;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3, p, label { color: #00FF41 !important; text-shadow: 0 0 8px #00FF41; }
    .stButton>button {
        background-color: #000000 !important;
        color: #00FF41 !important;
        border: 1px solid #00FF41 !important;
        font-weight: bold;
        width: 100%;
        margin-top: 10px;
    }
    .solution-box {
        background-color: rgba(0, 255, 65, 0.05);
        border: 1px solid #00FF41;
        padding: 20px;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR: CAREER INTELLIGENCE ---
st.sidebar.title("🚀 MISSION CONTROL")
today = datetime.date.today()
june_start = datetime.date(2026, 6, 1)

if today < june_start:
    st.sidebar.warning(f"LAUNCH IN: {(june_start - today).days} DAYS")
else:
    st.sidebar.success("SQUADRON ACTIVE")

st.sidebar.markdown("---")
st.sidebar.write("**LEVEL 02 OBJECTIVES:**")
st.sidebar.write("1. Master Calculus-based Physics")
st.sidebar.code("2. Data Visualization (Python)")
st.sidebar.write("3. Logical Syllogisms (CUET)")

# --- TUTORIAL ENGINE ---
def load_curriculum():
    tasks = {}
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    d, q, a = parts
                    if d not in tasks: tasks[d] = []
                    tasks[d].append({"q": q, "a": a})
    except:
        # Fallback if file is missing
        tasks["2026-06-01"] = [{"q": "Initialize System", "a": "System Ready. Load June 2+ data in questions.txt"}]
    return tasks

db = load_curriculum()

# --- DATE SELECTOR (FOR TESTING OR DAILY USE) ---
st.title("📟 ANALYST STUDY TERMINAL")
selected_date = st.select_slider("SELECT STUDY TIMELINE", 
                               options=["2026-06-01", "2026-06-02", "2026-06-03"],
                               value="2026-06-01")

st.markdown(f"### 📍 CURRICULUM DATE: {selected_date}")

if selected_date in db:
    for i, task in enumerate(db[selected_date]):
        st.subheader(f"⚡ PROBLEM SET {i+1}")
        st.info(task['q'])
        
        if st.button(f"EXECUTE TUTORIAL SOLUTION {i+1}"):
            st.markdown("<div class='solution-box'>", unsafe_allow_html=True)
            st.write("### 📝 STEP-BY-STEP ANALYSIS")
            # This renders LaTeX and text correctly
            st.write(task['a'])
            st.markdown("</div>", unsafe_allow_html=True)
else:
    st.error(f"DATA NOT FOUND FOR {selected_date}. Please update questions.txt.")
