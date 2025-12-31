import streamlit as st
import random
import datetime

# --- CONFIGURATION (The "Brain" of the App) ---
st.set_page_config(page_title="Harshit's CEO Protocol", page_icon="🚀")

# 1. DEFINE THE TASKS (Database)
# I've added your specific "Boss Coder" and "Swimming" interests here

# "CORE" - Deep Work (Career & CEO Goals)
career_tasks = [
    "Boss Coder: Solve 1 problem on 2D Arrays [Python]",
    "Read 10 pages of 'High Output Management' or 'Deep Work'",
    "Write a 150-word script for a potential TEDx talk",
    "Review 'BharatPe' product journey and write 3 lessons learned",
    "Analyze a new Fintech regulation from RBI",
    "Update LinkedIn: Share a product learning (No virality chasing)"
]

# "SOUL" - Holistic Growth (Relationships, Health, Giving back)
soul_tasks = [
    "Plan a thoughtful date idea (Relationship Goal)", 
    "Research a local NGO/Social Cause for weekend volunteering",
    "Go for a swim (if Summer) OR 30 min Walk without phone",
    "Cook a new meal from scratch (Therapeutic)",
    "Call a friend/family member just to listen (Interpersonal Skill)",
    "Complete 1 lesson on Duolingo (Language)"
]

# "IMPULSE" - Quick dopamine hits for when you feel bored/distracted
impulse_activities = [
    "Watch a movie trailer for an upcoming film",
    "Read 1 random article on Psychology Today",
    "Do a 2-minute breathing exercise",
    "Write down 3 things you are grateful for right now",
    "Watch a 5-min snippet of a Stand-up Comedy"
]

# --- THE APP LAYOUT (The User Interface) ---

# Title and Greeting
st.title("🚀 The CEO Protocol: Harshit's Journey")
st.write(f"**Current Focus:** CEO by 32 | Status: {datetime.date.today()}")

# Sidebar for Profile
st.sidebar.header("Profile: Harshit")
st.sidebar.write("• **Role:** Sr. PM (Fintech)")
st.sidebar.write("• **Mission:** 0.0001% Growth")
st.sidebar.write("• **Current Tech:** Python (Arrays)")

st.sidebar.markdown("---")
st.sidebar.write("Quote of the day:")
st.sidebar.info("'Calm beats hustle. Long game only.'")

# Main Section: The Daily 2
st.header("🎯 Your Daily Objectives")
st.write("Remember: Consistency > Intensity. Just 45 mins today.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. The Builder (Career)")
    # Logic: Pick a random task based on the day to keep it fresh
    today_career = random.choice(career_tasks)
    st.info(f"👉 {today_career}")
    if st.button("Mark Career Done"):
        st.success("Great job! That's 1% better.")
        st.balloons()

with col2:
    st.subheader("2. The Monk (Soul)")
    today_soul = random.choice(soul_tasks)
    st.info(f"👉 {today_soul}")
    if st.button("Mark Soul Done"):
        st.success("Balance achieved.")

# The "Impulsive Brain" Section
st.markdown("---")
st.subheader("🧠 Feeling Impulsive / Distracted?")
st.write("Don't quit. Just switch gears.")

if st.button("🎲 Give me a random fun task"):
    surprise = random.choice(impulse_activities)
    st.warning(f"**Your Surprise Task:** {surprise}")

# Reflection Area
st.markdown("---")
with st.expander("📝 Daily Reflection (Click to open)"):
    st.text_area("What is one decision you avoided today?")
