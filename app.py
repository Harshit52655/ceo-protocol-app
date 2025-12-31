import streamlit as st
import random

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's Mood OS", page_icon="🦁", layout="wide")

# --- 1. THE MOOD MATRIX (The Brain) ---
# This maps your mood to specific types of activities.
mood_matrix = {
    "🔥 High Energy": {
        "ceo_task": [
            {"title": "Financial Literacy: Study P&L Deep Dive", "url": "https://online.hbs.edu/blog/post/how-to-read-a-profit-and-loss-statement"},
            {"title": "Strategy: 7 Powers (Heavy Reading)", "url": "https://www.lennysnewsletter.com/p/7-powers-hamilton-helmer"},
            {"title": "System Design: Map out a delegation workflow", "url": "#"}
        ],
        "spirit": ["Chanting (Loud & Energetic)", "Power Yoga / Surya Namaskar", "Call a Mentor (High stakes)"],
        "leela": ["High Intensity Dance (Bollywood)", "100 Pushups/Jacks", "Go for a Run"]
    },
    "🔋 Low Battery": {
        "ceo_task": [
            {"title": "Light Reading: Tech Trends", "url": "https://techcrunch.com/"},
            {"title": "Watch: Steve Jobs Storytelling (Passive)", "url": "https://www.youtube.com/watch?v=9tnd97G5P2g"},
            {"title": "Review: Look at old notes (Low effort)", "url": "#"}
        ],
        "spirit": ["Yoga Nidra (Sleep Meditation)", "Listen to soothing Bhajan", "Gratitude Journaling (3 lines)"],
        "leela": ["Listen to Acoustic Music", "Watch a comforting movie trailer", "Stretching (Gentle)"]
    },
    "😰 Anxious / Overwhelmed": {
        "ceo_task": [
            {"title": "Organization: Clean Desktop/Email (Control)", "url": "#"},
            {"title": "Planning: Write tomorrow's To-Do list", "url": "#"},
            {"title": "Read: 'The Psychological Price of Entrepreneurship'", "url": "https://www.inc.com/magazine/201309/jessica-bruder/psychological-price-of-entrepreneurship.html"}
        ],
        "spirit": ["Box Breathing (4-4-4-4)", "Read 1 page of Stoicism", "Silence (5 mins)"],
        "leela": ["Cook a comfort meal", "Walk in nature (No phone)", "Clean your room (Therapeutic)"]
    },
    "🎨 Creative": {
        "ceo_task": [
            {"title": "Brainstorm: 10 Ideas for a Startup", "url": "#"},
            {"title": "Write: 1 LinkedIn Post draft", "url": "#"},
            {"title": "Vision: Sketch your life at age 40", "url": "#"}
        ],
        "spirit": ["Visualize your future self", "Read Poetry/Gita", "Deep conversation with partner"],
        "leela": ["Cook a new recipe (Experiment)", "Paint / Draw / Doodle", "Explore new music genre"]
    }
}

# --- 2. SESSION STATE & CONFIG ---
if 'active_project' not in st.session_state:
    st.session_state.active_project = {"name": "Python (Boss Coder)", "hours_done": 12.0, "total_hours": 60}

if 'current_mood' not in st.session_state:
    st.session_state.current_mood = "🔥 High Energy"

# Helper to pick task based on mood
def get_task(category, mode="random"):
    # If mode is 'course', we always return the main project
    if category == "dharma" and mode == "course":
        proj = st.session_state.active_project
        return {
            "title": f"Continue: {proj['name']}",
            "desc": "The Main Mission.",
            "type": "Project",
            "is_course": True
        }
    
    # Otherwise, look at the mood matrix
    mood_data = mood_matrix[st.session_state.current_mood]
    
    if category == "dharma":
        item = random.choice(mood_data['ceo_task'])
        return {"title": item['title'], "desc": "CEO Skill", "url": item['url'], "is_course": False}
    elif category == "spirit":
        return {"title": random.choice(mood_data['spirit'])}
    elif category == "leela":
        return {"title": random.choice(mood_data['leela'])}

# Initialize Tasks if empty
if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "dharma": get_task("dharma", mode="course"),
        "spirit": get_task("spirit"),
        "leela": get_task("leela")
    }

# --- UI LAYOUT ---
st.title("🦁 Harshit's Life Protocol")

# MOOD SELECTOR (The New Feature)
st.write("### How are you feeling right now?")
selected_mood = st.selectbox("", list(mood_matrix.keys()), label_visibility="collapsed")

# If mood changes, auto-shuffle everything to match
if selected_mood != st.session_state.current_mood:
    st.session_state.current_mood = selected_mood
    st.session_state.tasks['dharma'] = get_task("dharma", mode="course") # Keep course as default
    st.session_state.tasks['spirit'] = get_task("spirit")
    st.session_state.tasks['leela'] = get_task("leela")
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
        st.session_state.tasks['dharma'] = get_task("dharma", mode="random")
        st.rerun()
    if c2.button("🔙 Back to Project"):
        st.session_state.tasks['dharma'] = get_task("dharma", mode="course")
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
        st.session_state.tasks['spirit'] = get_task("spirit")
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
        st.session_state.tasks['leela'] = get_task("leela")
        st.rerun()

# --- SIDEBAR: PROJECT SETTINGS (The "Dynamic Input" Feature) ---
with st.sidebar:
    st.header("🦁 Your Empire")
    
    # Progress Bar
    proj = st.session_state.active_project
    prog = min(proj['hours_done'] / proj['total_hours'], 1.0)
    st.write(f"**Focus:** {proj['name']}")
    st.progress(prog)
    st.caption(f"{int(proj['hours_done'])} / {proj['total_hours']} Hours")
    
    st.divider()
    
    # EDIT FORM: Change your project anytime
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
            st.session_state.tasks['dharma'] = get_task("dharma", mode="course")
            st.success("Project Updated!")
            st.rerun()
