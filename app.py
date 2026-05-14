import streamlit as st
import datetime

# --- CONFIG & THEME ---
st.set_page_config(page_title="CityAnalyst Pro", layout="wide")
st.markdown("<style>.stApp {background: #1C2C5B; color: white;}</style>", unsafe_allow_html=True)

# --- MAN CITY PLAYER DATABASE ---
# In a real job, this would come from a Live API. For now, we build the "Master Sheet".
city_squad = {
    "Erling Haaland": {"pos": "ST", "matches": 31, "goals": 27, "fitness": 85, "injury_risk": "Low"},
    "Kevin De Bruyne": {"pos": "CAM", "matches": 18, "goals": 4, "fitness": 65, "injury_risk": "High"},
    "Phil Foden": {"pos": "RW/CAM", "matches": 34, "goals": 19, "fitness": 92, "injury_risk": "Low"},
    "Rodri": {"pos": "CDM", "matches": 33, "goals": 7, "fitness": 70, "injury_risk": "Medium"},
    "Bernardo Silva": {"pos": "CM/RW", "matches": 30, "goals": 6, "fitness": 88, "injury_risk": "Low"},
    "Ruben Dias": {"pos": "CB", "matches": 28, "goals": 0, "fitness": 95, "injury_risk": "Low"}
}

upcoming_matches = [
    {"date": "2026-05-17", "opponent": "Real Madrid (UCL)", "venue": "Etihad"},
    {"date": "2026-05-21", "opponent": "Chelsea (PL)", "venue": "Stamford Bridge"},
]

# --- LOAD STUDY DATA ---
def load_tasks():
    tasks_dict = {}
    try:
        with open("questions.txt", "r") as f:
            for line in f:
                if "|" in line:
                    date, q, a = line.strip().split("|")
                    if date not in tasks_dict: tasks_dict[date] = []
                    tasks_dict[date].append({"q": q, "a": a})
    except:
        tasks_dict = {"2026-06-01": [{"q": "System: questions.txt not found!", "a": "Check GitHub"}]}
    return tasks_dict

# --- UI NAVIGATION ---
st.title("🛡️ CityAnalyst Performance Hub")
tab1, tab2, tab3 = st.tabs(["📚 Study Lab", "📊 Squad Analytics", "🏟️ Match Center"])

# --- TAB 1: STUDY LAB ---
with tab1:
    today = datetime.date.today().strftime("%Y-%m-%d")
    all_tasks = load_tasks()
    display_date = today if today in all_tasks else "2026-05-14" # Testing mode
    
    st.header(f"Daily Mission: {display_date}")
    if display_date in all_tasks:
        for i, item in enumerate(all_tasks[display_date]):
            with st.expander(f"Task {i+1}: {item['q'][:30]}..."):
                st.write(item['q'])
                if st.button(f"Reveal Solution {i+1}"):
                    st.success(item['a'])
    else:
        st.info("No study tasks for today. Focus on scouting!")

# --- TAB 2: SQUAD ANALYTICS ---
with tab2:
    st.header("Player Performance & Medical Report")
    selected_player = st.selectbox("Select Player to Analyse", list(city_squad.keys()))
    
    p_data = city_squad[selected_player]
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Position", p_data["pos"])
    col2.metric("Matches Played", p_data["matches"])
    col3.metric("Goals/Assists", p_data["goals"])

    st.subheader("Health & Injury Risk")
    # Health Bar
    st.write(f"**Current Fitness:** {p_data['fitness']}%")
    st.progress(p_data['fitness'])
    
    if p_data['injury_risk'] == "High":
        st.error(f"⚠️ CRITICAL RISK: {selected_player} shows signs of hamstring fatigue. Recommended: Rest.")
    elif p_data['injury_risk'] == "Medium":
        st.warning(f"🟡 CAUTION: {selected_player} has high minute accumulation. Monitor load.")
    else:
        st.success(f"🟢 READY: {selected_player} is at peak physical condition.")

# --- TAB 3: MATCH CENTER ---
with tab3:
    st.header("Fixture List & Lineup Fixer")
    
    # Upcoming Match List
    for match in upcoming_matches:
        st.write(f"⚽ **{match['date']}** vs {match['opponent']} ({match['venue']})")
    
    st.divider()
    
    st.subheader("Starting XI Builder")
    st.write("Select your tactical lineup based on fitness and stats:")
    
    available_players = list(city_squad.keys())
    lineup = st.multiselect("Pick your Starting 11", available_players, default=available_players[:3])
    
    if len(lineup) > 11:
        st.error("Too many players! A team can only have 11.")
    else:
        st.info(f"Currently Selected: {len(lineup)}/11 players.")
        
    if st.button("Finalise Tactical Sheet"):
        st.balloons()
        st.write("### Tactical Summary")
        for p in lineup:
            risk = city_squad[p]['injury_risk']
            st.write(f"- **{p}** ({city_squad[p]['pos']}) | Risk Level: {risk}")
