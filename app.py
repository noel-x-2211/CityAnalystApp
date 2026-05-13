import streamlit as st
import datetime

# --- 1. PREMIUM LOOK & FEEL ---
st.set_page_config(page_title="CityAnalyst Pro", layout="wide")

# CSS for a Stunning Background and Glass UI
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
        url("https://images.unsplash.com/photo-1522778119026-d647f0596c20?ixlib=rb-4.0.3&auto=format&fit=crop&w=2070&q=80");
        background-size: cover;
        background-attachment: fixed;
    }
    
    /* Transparent "Glass" Cards for content */
    div.stText, div.stMarkdown, section.main .block-container {
        color: white !important;
    }

    /* Styling the Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(28, 44, 91, 0.8) !important;
        backdrop-filter: blur(10px);
    }

    /* Styling Buttons */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #6CABDD !important;
        color: white !important;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #5992bd !important;
        transform: scale(1.02);
    }

    /* Question Expanders */
    .streamlit-expanderHeader {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. THE DATA (Your Lifelong Database) ---
daily_db = {
    "2026-05-13": [
        {"q": "Today's Task: Finish setting up the App UI", "a": "COMPLETED! ✅"},
        {"q": "Goal: IIT Madras Application Status", "a": "Apply before May 31st!"}
    ],
    "2026-06-01": [
        {"q": "Math: If f(x) = x^2 + 3, find f(5).", "a": "28"},
        {"q": "Stats: Mean of Haaland's goals (1, 0, 2)?", "a": "1.0"},
        {"q": "Logic: If 'Start' is True and 'Fit' is False, what is (Start AND Fit)?", "a": "False"},
        {"q": "Math: Solve for x: 10^x = 100", "a": "2"},
        {"q": "Comp Thinking: What do you call a loop that never ends?", "a": "Infinite Loop"},
        {"q": "English: Synonym of 'Predict'?", "a": "Forecast"},
        {"q": "Stats: If a player scores 2 goals in 4 shots, what is the conversion rate?", "a": "50%"},
        {"q": "Math: Derivative of 5x?", "a": "5"},
        {"q": "Logic: Which gate gives True only if both inputs are True?", "a": "AND Gate"},
        {"q": "Comp Thinking: A diamond shape in a flowchart represents what?", "a": "Decision"},
        {"q": "Math: Area of a circle with radius 7? (Use 22/7)", "a": "154"},
        {"q": "Stats: The middle value in a sorted list is called?", "a": "Median"},
        {"q": "English: Antonym of 'Aggressive'?", "a": "Passive"},
        {"q": "Logic: Is (NOT True) equivalent to False?", "a": "Yes"},
        {"q": "Comp Thinking: First step in solving any problem with code?", "a": "Algorithm Design"}
    ]
}

# --- 3. SIDEBAR ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/e/eb/Manchester_City_FC_badge.svg", width=100)
st.sidebar.title("CityAnalyst Pro")
page = st.sidebar.radio("Navigate", ["🏠 Home", "📚 Daily Study", "⚽ Match Scout"])

# --- 4. DATE LOGIC ---
today_str = datetime.date.today().strftime("%Y-%m-%d")

# --- 5. PAGES ---
if page == "🏠 Home":
    st.title("🏆 Performance Analytics Hub")
    st.subheader(f"Session: {today_str}")
    st.write("---")
    st.write("### Your Career Path:")
    st.success("📍 Step 1: Python Basics (COMPLETED)")
    st.info("📍 Step 2: IIT Madras Qualifier Prep (CURRENT)")
    st.warning("📍 Step 3: Performance Analyst Internship (FUTURE)")

elif page == "📚 Daily Study":
    st.title("📖 Study Lab")
    
    # Check if date exists in DB
    if today_str in daily_db:
        tasks = daily_db[today_str]
    else:
        st.info("Showing Kickoff Prep (June 1st Data)")
        tasks = daily_db["2026-06-01"]

    for i, item in enumerate(tasks):
        with st.expander(f"Task {i+1}"):
            st.write(item["q"])
            if st.button(f"Reveal Solution {i+1}"):
                st.write(f"**Answer:** {item['a']}")

elif page == "⚽ Match Scout":
    st.title("🔍 Advanced Scouting")
    col1, col2 = st.columns(2)
    with col1:
        player = st.text_input("Enter Player", "Kevin De Bruyne")
        fitness = st.slider("Fitness Score", 0, 100, 85)
    with col2:
        match_importance = st.select_slider("Match Importance", options=["Low", "Medium", "High", "Final"])
    
    if st.button("Generate Tactical Verdict"):
        if fitness > 80 or match_importance == "Final":
            st.balloons()
            st.success(f"MUST START: {player} is vital for this fixture.")
        else:
            st.warning(f"ROTATE: Keep {player} on the bench for load management.")