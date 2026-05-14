import streamlit as st
import datetime
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="CityAnalyst Master Terminal", layout="wide")

# --- DATABASE: FULL 2026-2027 SQUAD ---
squad = {
    "G. Donnarumma": {"pos": "GK", "no": 25, "health": 100, "goals": 0, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 0, "heat": [1,1,1,1]},
    "James Trafford": {"pos": "GK", "no": 1, "health": 95, "goals": 0, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 0, "heat": [1,1,1,1]},
    "Ruben Dias": {"pos": "CB", "no": 3, "health": 98, "goals": 1, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 2, "heat": [2,8,2,1]},
    "John Stones": {"pos": "CB", "no": 5, "health": 72, "goals": 2, "risk": "High", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 5, "heat": [3,7,4,1]},
    "Marc Guéhi": {"pos": "CB", "no": 15, "health": 96, "goals": 2, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 1, "heat": [2,9,1,1]},
    "Manuel Akanji": {"pos": "CB/RB", "no": 25, "health": 94, "goals": 3, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 4, "heat": [3,6,3,1]},
    "Josko Gvardiol": {"pos": "LB/CB", "no": 24, "health": 91, "goals": 4, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 12, "heat": [4,5,8,4]},
    "R. Ait-Nouri": {"pos": "LB", "no": 21, "health": 89, "goals": 4, "risk": "Medium", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 18, "heat": [2,4,9,6]},
    "Rico Lewis": {"pos": "RB/CDM", "no": 82, "health": 99, "goals": 2, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 25, "heat": [2,6,7,5]},
    "Rodri": {"pos": "CDM", "no": 16, "health": 75, "goals": 6, "risk": "High", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 30, "heat": [1,9,9,2]},
    "Mateo Kovacic": {"pos": "CM", "no": 8, "health": 88, "goals": 4, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 15, "heat": [2,7,8,3]},
    "Bernardo Silva": {"pos": "CM/RW", "no": 20, "health": 90, "goals": 7, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 55, "heat": [2,5,9,9]},
    "Phil Foden": {"pos": "RW/AM", "no": 47, "health": 92, "goals": 21, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 68, "heat": [1,4,8,9]},
    "James McAtee": {"pos": "AM", "no": 87, "health": 97, "goals": 5, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 22, "heat": [1,3,7,8]},
    "Jeremy Doku": {"pos": "LW", "no": 11, "health": 82, "goals": 8, "risk": "Medium", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 40, "heat": [1,2,6,9]},
    "Savinho": {"pos": "RW/LW", "no": 26, "health": 94, "goals": 11, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 35, "heat": [1,3,7,9]},
    "Oscar Bobb": {"pos": "RW", "no": 52, "health": 94, "goals": 9, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 28, "heat": [1,2,8,8]},
    "Erling Haaland": {"pos": "ST", "no": 9, "health": 80, "goals": 38, "risk": "Medium", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 10, "heat": [0,1,3,9]},
    "Omar Marmoush": {"pos": "LW/ST", "no": 7, "health": 95, "goals": 14, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 32, "heat": [1,2,7,9]},
    "A. Semenyo": {"pos": "RW/ST", "no": 42, "health": 88, "goals": 10, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 25, "heat": [1,3,6,8]},
    "Matheus Nunes": {"pos": "CM", "no": 27, "health": 90, "goals": 2, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 18, "heat": [2,6,8,4]},
    "Josh Wilson-Esbrand": {"pos": "LB", "no": 30, "health": 100, "goals": 0, "risk": "Low", "img": "https://cdn-icons-png.flaticon.com/512/1165/1165248.png", "chances": 5, "heat": [3,4,6,2]},
}

# --- THEME ENGINE ---
def apply_theme(mode):
    if mode == "Football":
        st.markdown(f"""
            <style>
            .stApp {{
                background: linear-gradient(rgba(108, 171, 221, 0.75), rgba(28, 44, 91, 0.9)), 
                            url("https://www.mancity.com/dist/images/logos/man-city-logo.svg") no-repeat center;
                background-size: 550px; background-attachment: fixed; transition: all 0.6s ease;
            }}
            .p-card {{ background: rgba(255,255,255,0.1); border-radius: 10px; padding: 10px; border: 1px solid #6CABDD; margin-bottom: 5px; }}
            h1, h2, h3, p {{ color: white !important; text-shadow: 2px 2px 4px #000; }}
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .stApp {{ background: #000; color: #00FF41 !important; font-family: 'Courier New'; transition: all 0.6s ease; }}
            .stApp::before {{ content: ""; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, rgba(0,255,65,0.05) 1px, transparent 1px); background-size: 25px 25px; pointer-events: none; }}
            h1, h2, h3, p, span {{ color: #00FF41 !important; text-shadow: 0 0 5px #00FF41; }}
            </style>
        """, unsafe_allow_html=True)

# --- APP NAVIGATION ---
st.sidebar.markdown(f'<img src="https://www.mancity.com/dist/images/logos/man-city-logo.svg" width="80">', unsafe_allow_html=True)
nav = st.sidebar.radio("ACCESS LEVEL", ["FOOTBALL SCOUT", "STUDY LAB"])

if nav == "FOOTBALL SCOUT":
    apply_theme("Football")
    st.title("🛡️ CITY PERFORMANCE TERMINAL")
    
    t1, t2, t3 = st.tabs(["PLAYER PROFILES", "TACTICAL PITCH", "FIXTURES"])

    with t1:
        sel = st.selectbox("Select Player", list(squad.keys()))
        p = squad[sel]
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(p['img'], width=150)
            st.metric("Jersey No.", p['no'])
            if p['risk'] != "Low": st.error(f"MEDICAL ALERT: {p['risk']} Risk")
        with col2:
            st.subheader(f"Data Set: {sel}")
            st.write(f"**Position:** {p['pos']} | **Fitness:** {p['health']}%")
            st.metric("Goals/Assists", p['goals'])
            st.write("**Activity Heatmap (Efficiency Trend)**")
            st.area_chart(p['heat'])

    with t2:
        st.subheader("Starting XI Tactical Board")
        # Creating a more visual pitch grid
        starters = st.multiselect("Select your XI (Drag to reorder)", list(squad.keys()), default=list(squad.keys())[:11])
        
        # VISUAL PITCH REPRESENTATION
        st.markdown("""<div style='background: #1b5e20; height: 350px; border: 4px solid white; border-radius: 15px; position: relative;'>
            <div style='position: absolute; top: 10%; left: 45%; border: 2px solid white; width: 60px; height: 30px;'></div>
            <div style='position: absolute; bottom: 10%; left: 45%; border: 2px solid white; width: 60px; height: 30px;'></div>
            <div style='position: absolute; top: 50%; left: 0; width: 100%; border-top: 2px solid white; opacity: 0.3;'></div>
            <p style='text-align: center; color: white; margin-top: 150px; font-weight: bold;'>TACTICAL VIEW: ETIHAD</p>
        </div>""", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.write("### 🏟️ ON PITCH")
            for player in starters:
                st.markdown(f"<div class='p-card'>🏃 {player} ({squad[player]['pos']})</div>", unsafe_allow_html=True)
        with c2:
            st.write("### 🪑 DUGOUT")
            for p_name in squad.keys():
                if p_name not in starters:
                    st.markdown(f"<div class='p-card' style='opacity: 0.6;'>👟 {p_name}</div>", unsafe_allow_html=True)

    with t3:
        st.subheader("2026 Season Schedule")
        st.info("📅 2026-05-17 | vs Real Madrid (UCL Semi) @ Etihad")
        st.info("📅 2026-05-24 | vs Liverpool (PL) @ Anfield")
        st.success("📅 2026-05-31 | FA CUP FINAL @ Wembley")

else:
    apply_theme("Study")
    st.title("📟 ANALYST STUDY LAB")
    st.sidebar.progress(15)
    st.sidebar.write("Target: 20 LPA Goal")

    # LOAD QUESTIONS LOGIC
    tasks = {}
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    date, q, a = parts
                    if date not in tasks: tasks[date] = []
                    tasks[date].append({"q": q, "a": a})
    except: st.warning("Connect 'questions.txt' for daily updates.")

    today = datetime.date.today().strftime("%Y-%m-%d")
    disp = today if today in tasks else "2026-06-01"
    
    st.write(f"**CORE SESSION ACTIVE: {disp}**")
    if disp in tasks:
        for i, t in enumerate(tasks[disp]):
            with st.expander(f"QUERY {i+1}: {t['q'][:40]}..."):
                st.write(t['q'])
                if st.button(f"DECRYPT_{i}"): st.success(t['a'])
    else:
        st.info("NO DATA IN THE BRAIN. SYSTEM IDLE.")
