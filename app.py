import streamlit as st
import random
import brain  # Importing our logic file
from mood_library import mood_matrix # Importing for the dropdown list

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's Mood OS", page_icon="🦁", layout="wide")

# --- SESSION STATE ---
if 'active_project' not in st.session_state:
    st.session_state.active_project = {"name": "Python (Boss Coder)", "hours_done": 12.0, "total_hours": 60}

if 'current_mood' not in st.session_state:
    st.session_state.current_mood = "🔥 High Energy"

# Initialize Tasks if empty (Using brain.py logic)
if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "dharma": brain.get_task("dharma", st.session_state.current_mood, st.session_state.active_project, mode="course"),
        "spirit": brain.get_task("spirit", st.session_state.current_mood, st.session_state.active_project),
        "leela": brain.get_task("leela", st.session_state.current_mood, st.session_state.active_project)
    }

# --- UI LAYOUT ---
st.title("🦁 Harshit's Life Protocol")

# MOOD SELECTOR
st.write("### How are you feeling right now?")
selected_mood = st.selectbox("", list(mood_matrix.keys()), label_visibility="collapsed")

# If mood changes, auto-shuffle everything
if selected_mood != st.session_state.current_mood:
    st.session_state.current_mood = selected_mood
    # Calls the BRAIN to get new tasks
    st.session_state.tasks['dharma'] = brain.get_task("dharma", st.session_state.current_mood, st.session_state.active_project, mode="course")
    st.session_state.tasks['spirit'] = brain.get_task("spirit", st.session_state.current_mood, st.session_state.active_project)
    st.session_state.tasks['leela'] = brain.get_task("leela", st.session_state.current_mood, st.session_state.active_project)
    st.rerun()

st.divider()

# COLUMNS
col1, col2, col3 = st.columns([1, 1, 1])

# --- 1. DHARMA (Duty) ---
with col1:
    st.subheader("⚔️ Dharma")
    t = st.session_state.tasks['dharma']
    
    with st.container(border=True):
        st.markdown(f"**{t['title']}**")
        if t.get('url') and t['url'] != "#":
            st.link_button("🔗 Open Resource", t['url'])
        
        if t.get('is_course'):
            if st.button("✅ Log 20 Mins"):
                st.session_state.active_project['hours_done'] += 0.33
                st.balloons()
                st.rerun()
        else:
            if st.button("✅ Mark Read"):
                st.success("Done.")

    # Shuffle Buttons
    c1, c2 = st.columns(2)
    if c1.button("🔄 Swap (Mood Based)"):
        st.session_state.tasks['dharma'] = brain.get_task("dharma", st.session_state.current_mood, st.session_state.active_project, mode="random")
        st.rerun()
    if c2.button("🔙 Back to Project"):
        st.session_state.tasks['dharma'] = brain.get_task("dharma", st.session_state.current_mood, st.session_state.active_project, mode="course")
        st.rerun()

# --- 2. SPIRIT (Roots) ---
with col2:
    st.subheader("🪷 Spirit")
    t = st.session_state.tasks['spirit']
    
    with st.container(border=True):
        st.markdown(f"**{t['title']}**")
        st.caption("15 Mins • Grounding")
        if st.button("🙏 Connected"):
            st.success("Peace.")
            
    if st.button("🔄 Shuffle Spirit"):
        st.session_state.tasks['spirit'] = brain.get_task("spirit", st.session_state.current_mood, st.session_state.active_project)
        st.rerun()

# --- 3. LEELA (Play) ---
with col3:
    st.subheader("💃 Leela")
    t = st.session_state.tasks['leela']
    
    with st.container(border=True):
        st.markdown(f"**{t['title']}**")
        st.caption("10 Mins • Play")
        if st.button("✨ Joy Felt"):
            st.write("✨")
            
    if st.button("🔄 Shuffle Joy"):
        st.session_state.tasks['leela'] = brain.get_task("leela", st.session_state.current_mood, st.session_state.active_project)
        st.rerun()

# --- SIDEBAR: PROJECT SETTINGS ---
with st.sidebar:
    st.header("🦁 Your Empire")
    
    proj = st.session_state.active_project
    prog = min(proj['hours_done'] / proj['total_hours'], 1.0)
    st.write(f"**Focus:** {proj['name']}")
    st.progress(prog)
    st.caption(f"{int(proj['hours_done'])} / {proj['total_hours']} Hours")
    
    st.divider()
    
    with st.expander("⚙️ Edit Active Project"):
        new_name = st.text_input("New Course/Goal Name", value=proj['name'])
        new_hours = st.number_input("Total Hours Required", value=int(proj['total_hours']))
        new_done = st.number_input("Hours Already Done", value=float(proj['hours_done']))
        
        if st.button("Update Project"):
            st.session_state.active_project = {
                "name": new_name,
                "total_hours": new_hours,
                "hours_done": new_done
            }
            # Update Dharma task to reflect new project name
            st.session_state.tasks['dharma'] = brain.get_task("dharma", st.session_state.current_mood, st.session_state.active_project, mode="course")
            st.success("Project Updated!")
            st.rerun()
