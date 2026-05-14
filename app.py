import streamlit as st
import datetime
import pandas as pd

# --- CONFIG & ADVANCED STYLING ---
st.set_page_config(page_title="CityAnalyst Ultra", layout="wide")

def local_css(tab_type):
    if tab_type == "Football":
        bg_url = "https://www.mancity.com/dist/images/logos/man-city-logo.svg"
        st.markdown(f"""
            <style>
            .stApp {{
                background: linear-gradient(rgba(28, 44, 91, 0.9), rgba(28, 44, 91, 0.9)), 
                            url("{bg_url}") no-repeat center;
                background-size: 400px;
                transition: all 0.5s ease-in-out;
            }}
            .player-card {{ background: rgba(108, 171, 221, 0.2); border-radius: 15px; padding: 20px; border: 1px solid #6CABDD; }}
            </style>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .stApp { background: #0E1117; color: #00FF41; font-family: 'Courier New', monospace; transition: all 0.5s ease-in-out; }
            </style>
            """, unsafe_allow_html=True)

# --- THE 2026 SQUAD DATABASE ---
# Updated: KDB removed. Added 2025/26 relevant players.
squad = {
    "Erling Haaland": {"pos": "ST", "no": 9, "health": 95, "chances": 12, "goals": 32, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Phil Foden": {"pos": "RW", "no": 47, "health": 92, "chances": 45, "goals": 18, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Rodri": {"pos": "CDM", "no": 16, "health": 88, "chances": 22, "goals": 8, "risk": "Medium", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Bernardo Silva": {"pos": "CM", "no": 20, "health": 90, "chances": 38, "goals": 7, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Ruben Dias": {"pos": "CB", "no": 3, "health": 98, "chances": 5, "goals": 1, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Ederson": {"pos": "GK", "no": 31, "health": 100, "chances": 2, "goals": 0, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Josko Gvardiol": {"pos": "LB", "no": 24, "health": 85, "chances": 15, "goals": 4, "risk": "Medium", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Jeremy Doku": {"pos": "LW", "no": 11, "health": 78, "chances": 28, "goals": 6, "risk": "High", "img": "https://img.icons8.com/color/144/football-player.png"},
    "John Stones": {"pos": "CB", "no": 5, "health": 70, "chances": 10, "goals": 2, "risk": "Medium", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Savinho": {"pos": "RW", "no": 26, "health": 94, "chances": 31, "goals": 9, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Mateo Kovacic": {"pos": "CM", "no": 8, "health": 82, "chances": 18, "goals": 3, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
}

# --- NAVIGATION ---
st.sidebar.title("CITY ANALYST PRO")
menu = st.sidebar.radio("Select Hub", ["🏟️ Football Scout", "🧠 Study Lab"])

if menu == "🏟️ Football Scout":
    local_css("Football")
    st.title("Performance & Scouting Portal")
    
    scout_tab1, scout_tab2, scout_tab3 = st.tabs(["Player Profiles", "Tactical Pitch", "Fixtures"])

    with scout_tab1:
        st.subheader("Deep Dive Analysis")
        selected = st.selectbox("Select Player to Inspect", list(squad.keys()))
        p = squad[selected]
        
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(p['img'], width=200)
            st.metric("Jersey No.", p['no'])
            st.write(f"**Position:** {p['pos']}")
        
        with col2:
            st.markdown(f"### {selected} Summary")
            c1, c2, c3 = st.columns(3)
            c1.metric("Goals", p['goals'])
            c2.metric("Chances Created", p['chances'])
            c3.metric("Fitness", f"{p['health']}%")
            
            st.write("**Last Match Heatmap (Simulated)**")
            # Simple Heatmap Representation
            heatmap_data = pd.DataFrame([[0, 1, 2], [1, 5, 2], [0, 2, 1]])
            st.caption("Concentrated activity in Final Third")
            st.bar_chart(heatmap_data)
            
            if p['risk'] == "High":
                st.error("⚠️ Injury Warning: High fatigue detected in recovery scans.")

    with scout_tab2:
        st.subheader("Starting XI & Sub Fixer")
        # Virtual Pitch Logic
        st.markdown("""
            <div style="background-color: #2e7d32; height: 300px; border-radius: 20px; border: 3px solid white; position: relative;">
                <div style="position: absolute; left: 50%; top: 10%; border: 2px solid white; height: 50px; width: 100px; transform: translateX(-50%);"></div>
                <div style="position: absolute; left: 50%; bottom: 10%; border: 2px solid white; height: 50px; width: 100px; transform: translateX(-50%);"></div>
                <p style="color: white; text-align: center; margin-top: 130px; font-weight: bold; opacity: 0.5;">VIRTUAL ETIHAD PITCH</p>
            </div>
        """, unsafe_allow_html=True)
        
        starters = st.multiselect("Select Starting XI", list(squad.keys()), default=list(squad.keys())[:5])
        subs = [p for p in squad.keys() if p not in starters]
        
        col_s1, col_s2 = st.columns(2)
        col_s1.write("### ✅ Lineup")
        for s in starters: col_s1.write(f"🏃 {s} ({squad[s]['pos']})")
        
        col_s2.write("### 🪑 Substitutes")
        for sub in subs: col_s2.write(f"👟 {sub}")

else:
    local_css("Study")
    st.title("Data Analyst Study Lab")
    st.write("System: Initializing NCERT & IITM Modules...")
    # Your study code from before goes here
