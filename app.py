import streamlit as st
import datetime
import pandas as pd

# --- CONFIG ---
st.set_page_config(page_title="CityAnalyst Ultra Pro", layout="wide")

# --- THEME ENGINE (Backgrounds & Transitions) ---
def apply_theme(mode):
    if mode == "Football":
        # Transparent Sky Blue with Man City Logo
        st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(rgba(108, 171, 221, 0.7), rgba(28, 44, 91, 0.85)), 
                            url("https://www.mancity.com/dist/images/logos/man-city-logo.svg") no-repeat center;
                background-size: 500px;
                background-attachment: fixed;
                transition: all 0.8s ease-in-out;
            }
            [data-testid="stHeader"] { background: rgba(0,0,0,0); }
            .stMarkdown, p, h1, h2, h3 { color: white !important; text-shadow: 1px 1px 2px black; }
            </style>
        """, unsafe_allow_html=True)
    else:
        # Data Analyst / Matrix Theme
        st.markdown("""
            <style>
            .stApp {
                background-color: #050505;
                background-image: linear-gradient(0deg, transparent 24%, rgba(0, 255, 65, .05) 25%, rgba(0, 255, 65, .05) 26%, transparent 27%, transparent 74%, rgba(0, 255, 65, .05) 75%, rgba(0, 255, 65, .05) 76%, transparent 77%, transparent), linear-gradient(90deg, transparent 24%, rgba(0, 255, 65, .05) 25%, rgba(0, 255, 65, .05) 26%, transparent 27%, transparent 74%, rgba(0, 255, 65, .05) 75%, rgba(0, 255, 65, .05) 76%, transparent 77%, transparent);
                background-size: 50px 50px;
                color: #00FF41 !important;
                font-family: 'Courier New', Courier, monospace;
                transition: all 0.8s ease-in-out;
            }
            .stMarkdown, p, h1, h2, h3 { color: #00FF41 !important; }
            button { border: 1px solid #00FF41 !important; background: black !important; color: #00FF41 !important; }
            </style>
        """, unsafe_allow_html=True)

# --- 2026-2027 SQUAD DATABASE ---
squad = {
    "G. Donnarumma": {"pos": "GK", "no": 25, "health": 100, "goals": 0, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "James Trafford": {"pos": "GK", "no": 1, "health": 100, "goals": 0, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Ruben Dias": {"pos": "CB", "no": 3, "health": 98, "goals": 1, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Josko Gvardiol": {"pos": "LB/CB", "no": 24, "health": 91, "goals": 3, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Marc Guéhi": {"pos": "CB", "no": 15, "health": 96, "goals": 2, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "R. Ait-Nouri": {"pos": "LB", "no": 21, "health": 89, "goals": 4, "risk": "Medium", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Rodri": {"pos": "CDM", "no": 16, "health": 75, "goals": 6, "risk": "High", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Phil Foden": {"pos": "RW/AM", "no": 47, "health": 92, "goals": 21, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Erling Haaland": {"pos": "ST", "no": 9, "health": 80, "goals": 38, "risk": "Medium", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Omar Marmoush": {"pos": "LW/ST", "no": 7, "health": 95, "goals": 14, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "A. Semenyo": {"pos": "RW/LW", "no": 42, "health": 88, "goals": 10, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "James McAtee": {"pos": "AM", "no": 87, "health": 97, "goals": 5, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Oscar Bobb": {"pos": "RW", "no": 52, "health": 94, "goals": 8, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
    "Savinho": {"pos": "RW", "no": 26, "health": 90, "goals": 11, "risk": "Low", "img": "https://img.icons8.com/color/144/football-player.png"},
}

# --- QUESTIONS LOADER ---
def load_tasks():
    tasks = {}
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    date, q, a = parts
                    if date not in tasks: tasks[date] = []
                    tasks[date].append({"q": q, "a": a})
    except: pass
    return tasks

# --- UI NAVIGATION ---
st.sidebar.image("https://www.mancity.com/dist/images/logos/man-city-logo.svg", width=100)
nav = st.sidebar.radio("SYSTEM ACCESS", ["FOOTBALL SCOUT", "STUDY LAB"])

if nav == "FOOTBALL SCOUT":
    apply_theme("Football")
    st.title("🛡️ PERFORMANCE SCOUTING TERMINAL")
    
    t1, t2, t3 = st.tabs(["PLAYER PROFILES", "VIRTUAL PITCH", "MATCH SCHEDULE"])

    with t1:
        sel = st.selectbox("Select Player for Deep Analysis", list(squad.keys()))
        p = squad[sel]
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(p['img'], width=180)
            st.write(f"**No:** {p['no']} | **Pos:** {p['pos']}")
        with col2:
            st.subheader(f"Data Report: {sel}")
            c_a, c_b = st.columns(2)
            c_a.metric("Season Goals", p['goals'])
            c_b.metric("Recovery Fitness", f"{p['health']}%")
            st.write("**Chances Created Heatmap**")
            st.line_chart([10, 25, 15, 40, 30]) # Mock heatmap trend
            if p['risk'] != "Low": st.error(f"FATIGUE ALERT: {p['risk']} risk detected.")

    with t2:
        st.subheader("Tactical Lineup Fixer")
        # Creating a 4-3-3 visual structure using columns
        starters = st.multiselect("Drag players into XI", list(squad.keys()), default=list(squad.keys())[:11])
        st.markdown("<div style='background: #2e7d32; height: 10px; border-radius: 5px;'></div>", unsafe_allow_html=True)
        col_st, col_su = st.columns(2)
        with col_st:
            st.write("### 🏟️ STARTING XI")
            for player in starters: st.write(f"**{squad[player]['pos']}** - {player}")
        with col_su:
            st.write("### 🪑 BENCH")
            for p_name in squad.keys():
                if p_name not in starters: st.write(p_name)

    with t3:
        st.subheader("Upcoming Fixtures: 2026 Season")
        fixtures = [
            {"date": "2026-05-17", "opp": "Real Madrid (UCL)", "loc": "Etihad"},
            {"date": "2026-05-24", "opp": "Liverpool (PL)", "loc": "Anfield"},
            {"date": "2026-05-31", "opp": "FA Cup Final", "loc": "Wembley"}
        ]
        for f in fixtures: st.info(f"📅 {f['date']} | vs {f['opp']} @ {f['loc']}")

else:
    apply_theme("Study")
    st.title("📟 DATA ANALYST STUDY LAB")
    
    # Progress towards 20 LPA Goal
    st.sidebar.write("### 🚀 20 LPA TRACKER")
    st.sidebar.progress(15)
    st.sidebar.caption("Current Level: Junior Analyst Prep")

    today = datetime.date.today().strftime("%Y-%m-%d")
    db = load_tasks()
    
    # Study Tab content - No longer empty!
    st.write(f"**AUTHENTICATING SESSION... DATE: {today}**")
    
    # Logic to show tasks
    display_date = today if today in db else "2026-06-01"
    if display_date in db:
        for i, task in enumerate(db[display_date]):
            with st.container():
                st.write(f"**QUERY_{i+1}:** {task['q']}")
                if st.button(f"EXECUTE SOLUTION {i+1}"):
                    st.success(f"OUTPUT: {task['a']}")
    else:
        st.warning("NO DATA FOUND FOR TODAY. UPLOAD 'questions.txt' TO GITHUB.")
