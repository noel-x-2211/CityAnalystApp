import streamlit as st
import datetime
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="CityAnalyst Master", layout="wide")

# --- DATABASE: THE COMPLETE 2026-2027 SQUAD ---
full_squad = {
    "G. Donnarumma": {"pos": "GK", "no": 25, "health": 100, "goals": 0},
    "James Trafford": {"pos": "GK", "no": 1, "health": 98, "goals": 0},
    "Ruben Dias": {"pos": "CB", "no": 3, "health": 95, "goals": 1},
    "John Stones": {"pos": "CB", "no": 5, "health": 70, "goals": 2},
    "Marc Guéhi": {"pos": "CB", "no": 15, "health": 96, "goals": 2},
    "Manuel Akanji": {"pos": "CB/RB", "no": 25, "health": 94, "goals": 3},
    "Josko Gvardiol": {"pos": "LB/CB", "no": 24, "health": 91, "goals": 4},
    "R. Ait-Nouri": {"pos": "LB", "no": 21, "health": 89, "goals": 4},
    "Rico Lewis": {"pos": "RB/CDM", "no": 82, "health": 99, "goals": 2},
    "Rodri": {"pos": "CDM", "no": 16, "health": 78, "goals": 6},
    "Mateo Kovacic": {"pos": "CM", "no": 8, "health": 85, "goals": 4},
    "Bernardo Silva": {"pos": "CM/RW", "no": 20, "health": 90, "goals": 7},
    "Phil Foden": {"pos": "RW/AM", "no": 47, "health": 92, "goals": 21},
    "James McAtee": {"pos": "AM", "no": 87, "health": 97, "goals": 5},
    "Jeremy Doku": {"pos": "LW", "no": 11, "health": 82, "goals": 8},
    "Savinho": {"pos": "RW/LW", "no": 26, "health": 94, "goals": 11},
    "Oscar Bobb": {"pos": "RW", "no": 52, "health": 94, "goals": 9},
    "Erling Haaland": {"pos": "ST", "no": 9, "health": 80, "goals": 38},
    "Omar Marmoush": {"pos": "LW/ST", "no": 7, "health": 95, "goals": 14},
    "A. Semenyo": {"pos": "RW/ST", "no": 42, "health": 88, "goals": 10},
    "Matheus Nunes": {"pos": "CM", "no": 27, "health": 90, "goals": 2},
    "Josh Wilson-Esbrand": {"pos": "LB", "no": 30, "health": 100, "goals": 0},
    "Stefan Ortega": {"pos": "GK", "no": 18, "health": 100, "goals": 0},
    "Nathan Aké": {"pos": "CB/LB", "no": 6, "health": 88, "goals": 3}
}

# --- THEME ENGINE ---
nav = st.sidebar.radio("CHOOSE HUB", ["FOOTBALL HUB", "STUDY LAB"])

if nav == "FOOTBALL HUB":
    st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(rgba(108, 171, 221, 0.8), rgba(28, 44, 91, 0.9)), 
                        url("https://www.mancity.com/dist/images/logos/man-city-logo.svg");
            background-size: 500px; background-repeat: no-repeat; background-position: center;
        }
        h1, h2, h3, p, .stMetric { color: white !important; }
        .p-card { background: rgba(255,255,255,0.1); padding: 10px; border-radius: 10px; border: 1px solid white; margin: 5px; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🛡️ CITY PERFORMANCE HUB")
    tab1, tab2 = st.tabs(["SQUAD ANALYTICS", "MATCH CENTER"])
    
    with tab1:
        st.subheader("Interactive Tactical Pitch")
        # Functional XI Builder
        xi = st.multiselect("Select 11 Players for the Pitch", list(full_squad.keys()), default=list(full_squad.keys())[:11])
        
        col_xi, col_bench = st.columns(2)
        with col_xi:
            st.write("### 🏟️ STARTING XI")
            for player in xi:
                st.markdown(f"<div class='p-card'>🏃 {player} ({full_squad[player]['pos']})</div>", unsafe_allow_html=True)
        with col_bench:
            st.write("### 🪑 BENCH")
            for p in full_squad:
                if p not in xi:
                    st.write(f"👟 {p} ({full_squad[p]['pos']})")

    with tab2:
        st.subheader("Upcoming 2026 Fixtures")
        st.info("📅 May 17: UCL Semi-Final vs Real Madrid")
        st.info("📅 May 24: PL Final Day vs Liverpool")
        st.success("📅 May 31: FA CUP FINAL")

else:
    # STUDY LAB THEME
    st.markdown("""
        <style>
        .stApp { background-color: #000000; color: #00FF41 !important; }
        .stMarkdown, p, h1, h2, h3, label { color: #00FF41 !important; font-family: 'Courier New'; }
        .stButton>button { background-color: #000; border: 1px solid #00FF41; color: #00FF41; width: 100%; }
        </style>
    """, unsafe_allow_html=True)
    
    st.title("🧠 DATA ANALYST STUDY LAB")
    st.sidebar.progress(15)
    st.sidebar.write("20 LPA Goal Progress")
    
    # Load Questions
    def load_qs():
        qs = {}
        try:
            with open("questions.txt", "r") as f:
                for line in f:
                    parts = line.strip().split("|")
                    if len(parts) == 3:
                        d, q, a = parts
                        if d not in qs: qs[d] = []
                        qs[d].append({"q": q, "a": a})
        except: pass
        return qs

    data = load_qs()
    today = datetime.date.today().strftime("%Y-%m-%d")
    show_date = today if today in data else "2026-06-01"
    
    st.write(f"### MISSION DATE: {show_date}")
    if show_date in data:
        for i, item in enumerate(data[show_date]):
            st.write(f"**Q{i+1}:** {item['q']}")
            if st.button(f"Show Solution {i+1}"):
                st.success(f"Answer: {item['a']}")
    else:
        st.error("No questions found. Please check your questions.txt format.")
