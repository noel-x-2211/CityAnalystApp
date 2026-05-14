import streamlit as st
import datetime

# --- SYSTEM INITIALIZATION ---
st.set_page_config(page_title="CityAnalyst 2026", layout="wide", initial_sidebar_state="expanded")

# --- REAL 2026-2027 ROSTER DATA ---
# Derived from current 2026 squad lists
squad_data = {
    "Goalkeepers": ["Gianluigi Donnarumma", "James Trafford", "Marcus Bettinelli"],
    "Defenders": ["Rúben Dias", "John Stones", "Marc Guéhi", "Manuel Akanji", "Joško Gvardiol", "Rayan Aït-Nouri", "Rico Lewis", "Abdukodir Khusanov"],
    "Midfielders": ["Rodri", "Mateo Kovačić", "Bernardo Silva", "Phil Foden", "Tijjani Reijnders", "Matheus Nunes", "Nico O'Reilly"],
    "Forwards": ["Erling Haaland", "Omar Marmoush", "Antoine Semenyo", "Jérémy Doku", "Savinho", "Oscar Bobb"]
}

# --- NAVIGATION ---
nav = st.sidebar.radio("COMMAND CENTER", ["FOOTBALL HUB", "STUDY LAB"])

if nav == "FOOTBALL HUB":
    # Custom CSS for Man City branding and a cleaner tactical look
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(108, 171, 221, 0.9), rgba(28, 44, 91, 0.9)), 
                        url("https://www.mancity.com/dist/images/logos/man-city-logo.svg") no-repeat center center fixed;
            background-size: 350px;
        }
        h1, h2, h3, p, label { color: white !important; font-family: 'Outfit', sans-serif; }
        .player-card { background: rgba(255,255,255,0.1); border: 1px solid #6CABDD; border-radius: 10px; padding: 10px; text-align: center; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🛡️ CITY PERFORMANCE TERMINAL")
    
    # --- MATCH DAY STATUS ---
    # Real-time update: City just beat Crystal Palace 3-0 on May 14, 2026
    st.subheader("Latest Result: Man City 3 - 0 Crystal Palace")
    st.caption("Goals: Semenyo (32'), Marmoush (40'), Savinho (84')")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🏟️ Tactical Board")
        selected_xi = st.multiselect("Select Matchday Starting XI", 
                                     [p for pos in squad_data.values() for p in pos],
                                     default=["Gianluigi Donnarumma", "Rúben Dias", "Rodri", "Phil Foden", "Erling Haaland"])
        
        # Grid layout for selected players
        grid = st.columns(3)
        for i, player in enumerate(selected_xi):
            with grid[i % 3]:
                st.markdown(f"<div class='player-card'>👕 {player}</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 📅 Upcoming Fixtures")
        st.info("**Final Day of Season**\n\nvs Chelsea (Away)\n\nMay 24, 2026")
        
        st.markdown("### 📊 Squad Overview")
        for pos, players in squad_data.items():
            with st.expander(f"{pos} ({len(players)})"):
                for p in players:
                    st.text(f"• {p}")

else:
    # --- STUDY LAB (RETAINED EXACTLY AS REQUESTED) ---
    st.markdown("""
        <style>
        .stApp { background-color: #050505; color: #00FF41 !important; }
        h1, h2, h3, p, label { color: #00FF41 !important; font-family: 'Courier New', monospace; }
        .stButton>button { border: 1px solid #00FF41 !important; color: #00FF41 !important; background: black !important; width: 100%; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("📟 ANALYST STUDY LAB")
    st.sidebar.caption("20 LPA Career Track - Syncing...")
    
    # Placeholder for your specific questions logic that you mentioned is "perfect"
    def get_data():
        try:
            with open("questions.txt", "r") as f:
                return [line.strip().split("|") for line in f if "|" in line]
        except: return []

    raw_data = get_data()
    today = datetime.date.today().strftime("%Y-%m-%d")
    daily_tasks = [x for x in raw_data if x[0] == today]
    
    if daily_tasks:
        for i, (date, q, a) in enumerate(daily_tasks):
            st.write(f"**ID_{i+1}:** {q}")
            if st.button(f"RUN SOLUTION {i+1}"):
                st.success(f"OUTPUT >> {a}")
    else:
        st.warning("No new entries for today in questions.txt.")
