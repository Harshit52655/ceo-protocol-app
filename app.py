import streamlit as st
import datetime
import pandas as pd
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's Growth Engine", page_icon="🦁", layout="wide")

# --- DATA: MOCK REAL-TIME RECOMMENDATIONS ---
# This dictionary acts as your "Smart Engine" database.
course_options = {
    "Python (Data Structures)": {
        "paid": {"name": "Boss Coder Academy", "url": "https://www.bosscoderacademy.com/", "cost": "Paid", "type": "Cohort"},
        "free": {"name": "CS50 by Harvard (EdX)", "url": "https://cs50.harvard.edu/x/", "cost": "Free", "type": "Self-paced"},
        "duration_hours": 60
    },
    "Product Management": {
        "paid": {"name": "Reforge / Lenny's Course", "url": "https://www.reforge.com/", "cost": "$$$", "type": "Deep Dive"},
        "free": {"name": "Y Combinator Startup School", "url": "https://www.startupschool.org/", "cost": "Free", "type": "Practical"},
        "duration_hours": 40
    },
    "Leadership & Strategy": {
        "paid": {"name": "Harvard Online: Strategy", "url": "https://online.hbs.edu/courses/strategy/", "cost": "$$$", "type": "Certificate"},
        "free": {"name": "Acquired Podcast + Hamilton Helmer 7 Powers", "url": "https://www.acquired.fm/", "cost": "Free", "type": "Audio"},
        "duration_hours": 20
    }
}

# --- SESSION STATE (Memory) ---
# This remembers your progress as long as the app is running.
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = 0 # Total days showed up (No Streak Anxiety)
if 'current_course' not in st.session_state:
    st.session_state.current_course = "Python (Data Structures)" # Default
if 'course_progress_hours' not in st.session_state:
    st.session_state.course_progress_hours = 0.0

# --- SIDEBAR: USER SETTINGS ---
with st.sidebar:
    st.header(f"🦁 Legend Score: {st.session_state.user_progress}")
    st.caption("Total days you invested in yourself (No pressure).")
    
    st.divider()
    st.subheader("🎓 Current Focus")
    # User selects what they want to learn
    selected_topic = st.selectbox("I want to learn:", list(course_options.keys()))
    
    # Update state if changed
    if selected_topic != st.session_state.current_course:
        st.session_state.current_course = selected_topic
        st.session_state.course_progress_hours = 0.0 # Reset progress for new topic
        st.rerun()

# --- MAIN DASHBOARD ---
st.title("The Growth Engine")
st.write(f"**Goal:** CEO by 32 | **Focus:** {st.session_state.current_course}")

# 1. THE SMART COURSE RECOMMENDATION ENGINE
st.subheader(f"1. Master: {st.session_state.current_course}")

# Fetch Data
course_data = course_options[st.session_state.current_course]
total_hours = course_data['duration_hours']
hours_done = st.session_state.course_progress_hours
percent_done = min(hours_done / total_hours, 1.0)

# Display Progress
st.progress(percent_done)
st.caption(f"Progress: {int(hours_done)} / {total_hours} Hours")

col1, col2 = st.columns(2)

# Option A: The "Commitment" (Paid/Current)
with col1:
    with st.container(border=True):
        st.write("💎 **Your Premium Path**")
        st.subheader(course_data['paid']['name'])
        st.write(f"Type: {course_data['paid']['type']}")
        st.link_button(f"Continue Course", course_data['paid']['url'])

# Option B: The "Explorer" (Free Alternative)
with col2:
    with st.container(border=True):
        st.write("🌱 **The Free Alternative**")
        st.subheader(course_data['free']['name'])
        st.write(f"Type: {course_data['free']['type']}")
        st.write("*Good for: Quick reference or second opinion.*")
        st.link_button(f"Check this out", course_data['free']['url'])

# Daily Action Logic
st.info(f"📅 **Today's Plan:** To finish this in 2 months, invest **45 mins** today.")

if st.button("✅ I did 45 mins of learning"):
    st.session_state.course_progress_hours += 0.75
    st.session_state.user_progress += 1
    st.balloons()
    st.rerun()

# 2. THE HOLISTIC CHECK-IN (Non-Negotiables)
st.divider()
st.subheader("2. The Non-Negotiables (Life Balance)")

c1, c2, c3 = st.columns(3)

with c1:
    st.write("❤️ **Relationship**")
    if st.button("Called/Messaged Partner"):
        st.toast("Relationship deposit made! 💍")

with c2:
    st.write("💪 **Health**")
    if st.button("Did 30 min Activity"):
        st.toast("Body energized! ⚡")

with c3:
    st.write("🌍 **Impact**")
    if st.button("Read Social Cause News"):
        st.toast("Perspective widened. 🌏")

# 3. REAL-TIME CONTENT FEED (Simulated)
st.divider()
st.subheader("📰 Fresh Reads for You")
st.caption("Curated based on your 'CEO by 32' Goal")

# This list simulates a "Daily Feed" that could come from an API later
feed = [
    {"source": "Harvard Biz Review", "title": "Why 30-year-old CEOs fail (and how to avoid it)", "tag": "Strategy"},
    {"source": "TechCrunch", "title": "The rise of AI in Fintech: What PMs need to know", "tag": "Industry"},
    {"source": "Psychology Today", "title": "Overcoming 'Imposter Syndrome' in High Growth Roles", "tag": "Mindset"}
]

for item in feed:
    with st.expander(f"{item['tag']}: {item['title']}"):
        st.write(f"Source: {item['source']}")
        st.write("Read this to stay ahead of the curve.")
