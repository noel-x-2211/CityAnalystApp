import streamlit as st
import datetime

# --- SYSTEM INITIALIZATION ---
st.set_page_config(page_title="CityAnalyst 2026", layout="wide", initial_sidebar_state="expanded")

# --- 100% COMPLETE 2026-2027 ROSTER ---
squad_data = {
    "GK": ["G. Donnarumma", "James Trafford", "Stefan Ortega"],
    "DEF": ["Ruben Dias", "John Stones", "Marc Guéhi", "Manuel Akanji", "Josko Gvardiol", "Rayan Ait-Nouri", "Rico Lewis", "Nathan Aké", "Abdukodir Khusanov"],
    "MID": ["Rodri", "Mateo Kovacic", "Bernardo Silva", "Phil Foden", "James McAtee", "Nico O'Reilly", "Tijjani Reijnders", "Matheus Nunes"],
    "FWD": ["Erling Haaland", "Omar Marmoush", "Antoine Semenyo", "Jeremy Doku", "Savinho", "Oscar Bobb", "Claudio Echeverri"]
}

# --- THEME ENGINE (FIXED) ---
nav = st.sidebar.radio("COMMAND CENTER", ["FOOTBALL HUB", "STUDY LAB"])

if nav == "FOOTBALL HUB":
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(108, 171, 221, 0.85), rgba(28, 44, 91, 0.95)), 
                        url("https://www.mancity.com/dist/images/logos/man-city-logo.svg") no-repeat center center fixed;
            background-size: 400px;
        }
        h1, h2, h3, p, label, .stMetric { color: white !important; font-family: 'Outfit', sans-serif; text-shadow: 1px 1px 2px black; }
        .pitch-card { background: rgba(255,255,255,0.15); border: 1px solid #6CABDD; border-radius: 8px; padding: 10px; margin: 5px 0; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🛡️ CITY PERFORMANCE TERMINAL")
    
    # --- TRUE TACTICAL BOARD ---
    st.subheader("Match Day Tactical Board")
    col_pitch, col_info = st.columns([2, 1])
    
    with col_pitch:
        # Visual Grid representing the pitch zones
        st.markdown("<div style='background:#2e7d32; padding:20px; border:3px solid white; border-radius:15px;'>", unsafe_allow_html=True)
        xi = st.multiselect("Draft Starting XI", [p for pos in squad_data.values() for p in pos], default=[squad_data["GK"][0]] + squad_data["DEF"][:4] + squad_data["MID"][:3] + squad_data["FWD"][:3])
        
        c1, c2, c3 = st.columns(3)
        for i, player in enumerate(xi):
            with [c1, c2, c3][i % 3]:
                st.markdown(f"<div class='pitch-card'>👕 {player}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col_info:
        st.write("### 📅 NEXT FIXTURE")
        st.info("**UCL SEMI-FINAL**\n\nvs Real Madrid @ Etihad\n\nMay 17, 2026")
        st.write("---")
        st.write("### 📊 SQUAD DEPTH")
        for pos, players in squad_data.items():
            with st.expander(f"{pos} - {len(players)} Players"):
                for p in players: st.write(f"• {p}")

else:
    # --- STUDY LAB ENGINE (FIXED) ---
    st.markdown("""
        <style>
        .stApp { background-color: #050505; color: #00FF41 !important; }
        h1, h2, h3, p, label { color: #00FF41 !important; font-family: 'Courier New', monospace; }
        .stButton>button { border: 1px solid #00FF41 !important; color: #00FF41 !important; background: black !important; width: 100%; }
        .stSuccess { background-color: #001a00 !important; color: #00FF41 !important; border: 1px solid #00FF41; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("📟 ANALYST STUDY LAB")
    st.sidebar.progress(15)
    st.sidebar.caption("20 LPA Career Track")

    # Question Logic
    def get_data():
        try:
            with open("questions.txt", "r") as f:
                return [line.strip().split("|") for line in f if "|" in line]
        except: return []

    raw_data = get_data()
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    # Auto-filter for today
    daily_tasks = [x for x in raw_data if x[0] == today]
    
    if daily_tasks:
        for i, (date, q, a) in enumerate(daily_tasks):
            st.write(f"**PROBLEM_ID_{i+1}:** {q}")
            if st.button(f"RUN SOLUTION {i+1}"):
                st.success(f"OUTPUT >> {a}")
    else:
        st.warning("SYSTEM STANDBY: No questions found for today. Verify 'questions.txt' on GitHub.")
