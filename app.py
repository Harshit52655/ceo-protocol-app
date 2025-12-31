import streamlit as st
import datetime
import pandas as pd
import random
from openai import OpenAI

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's AI Coach", page_icon="🧠", layout="wide")

# --- SESSION STATE INITIALIZATION ---
if 'user_progress' not in st.session_state:
    st.session_state.user_progress = 0
if 'current_course' not in st.session_state:
    st.session_state.current_course = "Python (Data Structures)" # The Anchor
if 'course_progress_hours' not in st.session_state:
    st.session_state.course_progress_hours = 0.0
if 'ai_plan' not in st.session_state:
    st.session_state.ai_plan = None # Stores the daily AI generation

# --- THE AI ENGINE ---
def get_ai_guidance(topic, hours_done):
    """
    This function sends a prompt to the AI.
    It enforces the 'No Drop' rule by feeding current progress.
    """
    
    # 1. Check for API Key (Secrets)
    api_key = st.secrets.get("OPENAI_API_KEY")
    
    if not api_key:
        return None # Fallback to manual library if no key
    
    client = OpenAI(api_key=api_key)
    
    # 2. The Strict "Continuity" Prompt
    prompt = f"""
    User Context:
    - Name: Harshit (Aspiring CEO, 30yo)
    - Current Active Goal: {topic}
    - Progress: {hours_done} hours completed so far.
    
    YOUR JOB:
    Act as a strict yet encouraging mentor.
    1. Do NOT suggest changing topics. Keep him on {topic}.
    2. Suggest exactly ONE specific sub-topic or exercise for today (45 mins).
    3. Explain WHY this specific step is the logical next step based on his progress.
    4. Provide a 'Eureka' thought related to this topic.
    
    Output Format:
    **Task:** [Task Name]
    **Why:** [Reasoning]
    **Eureka:** [Insight]
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # Or gpt-4 if you want to pay more
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return None

# --- SIDEBAR ---
with st.sidebar:
    st.header(f"🧠 AI Coach")
    st.write(f"**Focus:** {st.session_state.current_course}")
    
    # Allow changing focus, but warn user
    new_topic = st.selectbox("Change Focus (Careful!)", 
                             ["Python (Data Structures)", "Product Strategy", "Leadership", "Swimming"])
    
    if new_topic != st.session_state.current_course:
        st.warning("Switching topics resets your flow. Are you sure?")
        if st.button("Yes, I'm switching"):
            st.session_state.current_course = new_topic
            st.session_state.course_progress_hours = 0.0
            st.session_state.ai_plan = None # Reset plan
            st.rerun()

# --- MAIN DASHBOARD ---
st.title(f"🚀 Harshit's Protocol")
st.caption(f"Powered by AI • {datetime.date.today().strftime('%B %d, %Y')}")

# 1. GENERATE TODAY'S PLAN
if st.session_state.ai_plan is None:
    with st.spinner("AI is analyzing your progress and generating the next step..."):
        # Call the AI
        plan = get_ai_guidance(st.session_state.current_course, st.session_state.course_progress_hours)
        
        if plan:
            st.session_state.ai_plan = plan
        else:
            # FALLBACK (If no API Key or Error)
            st.session_state.ai_plan = f"""
            **Task:** Continue {st.session_state.current_course}
            **Why:** AI Key not found. Running in offline mode.
            **Eureka:** Consistency is the only algorithm that matters.
            """

# 2. DISPLAY THE PLAN
st.subheader("🎯 Today's AI Directive")
with st.container(border=True):
    st.markdown(st.session_state.ai_plan)

# 3. ACTION BUTTON
st.write("")
col1, col2 = st.columns([1, 4])
with col1:
    if st.button("✅ I did it (45 mins)"):
        st.session_state.course_progress_hours += 0.75
        st.session_state.user_progress += 1
        st.session_state.ai_plan = None # Clear plan so tomorrow gets a new one
        st.balloons()
        st.rerun()

# 4. PROGRESS VISUALIZER
st.divider()
st.caption("Journey Continuity")
# Visualizing that 'dropping' is not happening, just climbing
st.progress(min(st.session_state.course_progress_hours / 50.0, 1.0))
st.caption(f"You have invested {st.session_state.course_progress_hours} hours in {st.session_state.current_course}. Keep climbing.")

# 5. REFLECTION (Manual)
with st.expander("Add a Note to your AI Coach"):
    st.text_input("What was hard about today's task?")
