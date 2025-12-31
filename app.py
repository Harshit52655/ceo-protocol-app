import streamlit as st
import random
import datetime
import pandas as pd
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's CEO Protocol", page_icon="🚀")

# --- 1. CURATED DATABASE (The "Guru" Content) ---
# Instead of random text, we now have structured data with Titles and Links.

# CAREER: Strategic Thinking & CEO Mindset
career_library = [
    {"title": "Lesson: How to Be Strategic", "type": "Article", "url": "https://www.lennysnewsletter.com/p/how-to-be-strategic", "time": "10 min"},
    {"title": "Video: Steve Jobs on Managing People", "type": "Video", "url": "https://www.youtube.com/watch?v=f60dheI4ARg", "time": "15 min"},
    {"title": "Deep Work: The 3 Groups", "type": "Concept", "url": "https://calnewport.com/deep-work-rules-for-focused-success-in-a-distracted-world/", "time": "5 min"},
    {"title": "Code: Solve 'Rotate Image' (2D Matrix)", "type": "Python", "url": "https://leetcode.com/problems/rotate-image/", "time": "20 min"},
    {"title": "Essay: Maker's Schedule, Manager's Schedule", "type": "Essay", "url": "http://www.paulgraham.com/makersschedule.html", "time": "8 min"}
]

# SOUL: Psychology, Relationships, & Health
soul_library = [
    {"title": "Dating: The 36 Questions to Fall in Love", "type": "Action", "url": "https://www.nytimes.com/2015/01/09/style/no-37-big-wedding-or-small.html", "time": "Evening"},
    {"title": "Life: The Tail End (Perspective on Parents)", "type": "Read", "url": "https://waitbutwhy.com/2015/12/the-tail-end.html", "time": "10 min"},
    {"title": "Health: The Scientific 7-Minute Workout", "type": "Activity", "url": "https://well.blogs.nytimes.com/2013/05/09/the-scientific-7-minute-workout/", "time": "7 min"},
    {"title": "Psychology: The decision matrix", "type": "Mental Model", "url": "https://fs.blog/mental-models/", "time": "15 min"},
    {"title": "Giving: Effective Altruism Intro", "type": "Social Cause", "url": "https://www.effectivealtruism.org/articles/introduction-to-effective-altruism", "time": "12 min"}
]

# --- 2. GOOGLE SHEETS CONNECTION (The Brain) ---
# This function tries to load data from the cloud. If it fails (setup not done), it falls back to a "Demo Mode".

def load_data():
    try:
        # Try connecting to Google Sheets
        conn = st.connection("gsheets", type=GSheetsConnection)
        df = conn.read(worksheet="Sheet1")
        return df, conn
    except Exception:
        # Fallback if connection isn't set up yet
        return pd.DataFrame(columns=["Date", "Task", "Type", "Status"]), None

df, conn = load_data()

# --- 3. SESSION STATE (Short Term Memory) ---
if 'todays_career' not in st.session_state:
    st.session_state.todays_career = random.choice(career_library)
if 'todays_soul' not in st.session_state:
    st.session_state.todays_soul = random.choice(soul_library)

# --- 4. THE APP DASHBOARD ---
st.title("🚀 The CEO Protocol")
st.markdown(f"**Profile:** Harshit | **Focus:** CEO by 32 | **Date:** {datetime.date.today()}")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Build (Career)")
    task = st.session_state.todays_career
    st.info(f"**{task['type']}** ({task['time']})")
    st.markdown(f"### [{task['title']}]({task['url']})")
    
    if st.button("Mark Career Complete"):
        # Write to Google Sheet
        if conn:
            new_row = pd.DataFrame([{"Date": str(datetime.date.today()), "Task": task['title'], "Type": "Career", "Status": "Done"}])
            updated_df = pd.concat([df, new_row], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
            st.success("Saved to Cloud Database!")
        else:
            st.warning("Google Sheet not connected yet. (Check Setup Instructions)")

with col2:
    st.subheader("Nourish (Soul)")
    task = st.session_state.todays_soul
    st.info(f"**{task['type']}** ({task['time']})")
    st.markdown(f"### [{task['title']}]({task['url']})")
    
    if st.button("Mark Soul Complete"):
        # Write to Google Sheet
        if conn:
            new_row = pd.DataFrame([{"Date": str(datetime.date.today()), "Task": task['title'], "Type": "Soul", "Status": "Done"}])
            updated_df = pd.concat([df, new_row], ignore_index=True)
            conn.update(worksheet="Sheet1", data=updated_df)
            st.success("Saved to Cloud Database!")
        else:
            st.warning("Google Sheet not connected yet.")

# --- 5. PROGRESS SECTION ---
st.divider()
st.subheader("📊 Your Growth Log")
if not df.empty:
    st.dataframe(df)
else:
    st.write("No history found. Complete a task to start your streak.")
