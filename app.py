import streamlit as st
import random
import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's CEO Protocol", page_icon="🚀")

# --- DATABASE OF TASKS ---
career_tasks = [
    "Boss Coder: Solve 1 problem on 2D Arrays [Python]",
    "Read 10 pages of 'High Output Management'",
    "Write a 150-word script for a potential TEDx talk",
    "Review 'BharatPe' product journey and write 3 lessons learned",
    "Analyze a new Fintech regulation from RBI",
    "Update LinkedIn: Share a product learning (No virality chasing)"
]

soul_tasks = [
    "Plan a thoughtful date idea (Relationship Goal)", 
    "Research a local NGO/Social Cause for weekend volunteering",
    "Go for a swim (if Summer) OR 30 min Walk without phone",
    "Cook a new meal from scratch (Therapeutic)",
    "Call a friend/family member just to listen",
    "Complete 1 lesson on Duolingo (Language)"
]

impulse_activities = [
    "Watch a movie trailer for an upcoming film",
    "Read 1 random article on Psychology Today",
    "Do a 2-minute breathing exercise",
    "Write down 3 things you are grateful for right now",
    "Watch a 5-min snippet of a Stand-up Comedy"
]

# --- THE MEMORY SYSTEM (Session State) ---
# This 'backpack' keeps data persistent even when you click buttons.

if 'career_task' not in st.session_state:
    st.session_state.career_task = random.choice(career_tasks)

if 'soul_task' not in st.session_state:
    st.session_state.soul_task = random.choice(soul_tasks)

if 'streak' not in st.session_state:
    st.session_state.streak = 12  # Starting dummy streak for motivation!

if 'history' not in st.session_state:
    st.session_state.history = []

# --- THE APP UI ---

st.title("🚀 The CEO Protocol: Harshit's Journey")
st.write(f"**Current Focus:** CEO by 32 | Status: {datetime.date.today()}")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
st.sidebar.header(f"🔥 Streak: {st.session_state.streak} Days")
st.sidebar.write("• **Role:** Sr. PM (Fintech)")
st.sidebar.write("• **Tech:** Python (2D Arrays)")
st.sidebar.markdown("---")
st.sidebar.info("'Calm beats hustle. Long game only.'")

# Main Dashboard
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. The Builder (Career)")
    st.info(f"👉 {st.session_state.career_task}")
    
    if st.button("Mark Career Done"):
        st.session_state.history.append(f"✅ Career: {st.session_state.career_task}")
        st.success("Log added! 1% Better.")
        st.balloons()

with col2:
    st.subheader("2. The Monk (Soul)")
    st.info(f"👉 {st.session_state.soul_task}")
    
    if st.button("Mark Soul Done"):
        st.session_state.history.append(f"✅ Soul: {st.session_state.soul_task}")
        st.success("Balance achieved.")

# Impulse Section
st.markdown("---")
st.subheader("🧠 Impulse Control")
if st.button("🎲 I'm bored - give me a distraction"):
    surprise = random.choice(impulse_activities)
    st.warning(f"**Do this instead of scrolling:** {surprise}")

# Progress Log (Temporary Memory)
st.markdown("---")
with st.expander("📝 See Today's Log"):
    for item in st.session_state.history:
        st.write(item)
