import streamlit as st
import random
import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's Reality OS", page_icon="🦁", layout="wide")

# --- 1. THE MOOD MATRIX (Updated with SURVIVAL MODE) ---
mood_matrix = {
    "🔥 High Energy": {
        "dharma": [
            {"title": "Deep Work: P&L Analysis", "url": "https://online.hbs.edu/blog/post/how-to-read-a-profit-and-loss-statement"},
            {"title": "Strategy: Read 7 Powers", "url": "https://www.lennysnewsletter.com/p/7-powers-hamilton-helmer"},
            {"title": "Build: Python Logic Challenge", "url": "#"}
        ],
        "spirit": ["Power Yoga (Surya Namaskar)", "Call Mentor (Strategy)", "Chanting (Loud)"],
        "leela": ["High Intensity Interval (HIIT)", "Bollywood Dance Flow", "Run 2km"]
    },
    "🔋 Low Battery": {
        "dharma": [
            {"title": "Passive: Watch Steve Jobs Speech", "url": "https://www.youtube.com/watch?v=UF8uR6Z6KLc"},
            {"title": "Review: Read old notes", "url": "#"},
            {"title": "News: Scan TechCrunch Headlines", "url": "https://techcrunch.com/"}
        ],
        "spirit": ["Yoga Nidra (Lying down)", "Listen to Bhajan", "Gratitude (3 things)"],
        "leela": ["Acoustic Music Session", "Stretch (Gentle)", "Watch Movie Trailer"]
    },
    "😰 Anxious": {
        "dharma": [
            {"title": "Control: Clean Desktop/Files", "url": "#"},
            {"title": "Plan: Write tomorrow's Top 3", "url": "#"},
            {"title": "Read: 'The Struggle' by Ben Horowitz", "url": "https://a16z.com/the-struggle/"}
        ],
        "spirit": ["Box Breathing (4-4-4-4)", "Read Daily Stoic", "Silence (5 mins)"],
        "leela": ["Comfort Cook (Maggi/Tea)", "Walk without phone", "Clean Room"]
    },
    "🚑 Emergency (5 mins)": {
        "dharma": [
            {"title": "1-Min: Read one financial definition", "url": "https://www.investopedia.com/financial-term-dictionary-4769738"},
            {"title": "1-Min: Write one goal for tomorrow", "url": "#"}
        ],
        "spirit": ["1-Min: Close eyes & breathe", "1-Min: Text Mom 'Love you'"],
        "leela": ["1-Song Dance Party", "10 Jumping Jacks"]
    }
}

# --- 2. SESSION STATE ---
if 'active_project' not in st.session_state:
    st.session_state.active_project = {"name": "Python (Boss Coder)", "hours_done": 12.0, "total_hours": 60}
if 'current_mood' not in st.session_state:
    st.session_state.current_mood = "🔥 High Energy"
if 'journal_entry' not in st.session_state:
    st.session_state.journal_entry = ""

# --- HELPER FUNCTIONS ---
def get_task(category, mode="random"):
    mood_data = mood_matrix[st.session_state.current_mood]
    
    # Emergency mode override (It's always random, no course work)
    if st.session_state.current_mood == "🚑 Emergency (5 mins)":
        if category == "dharma": return {"title": random.choice(mood_data['dharma'])['title'], "url": "#", "is_course": False}
        if category == "spirit": return {"title": random.choice(mood_data['spirit'])}
        if category == "leela": return {"title": random.choice(mood_data['leela'])}

    # Normal Modes
    if category == "dharma" and mode == "course":
        proj = st.session_state.active_project
        return {"title": f"Continue: {proj['name']}", "desc": "The Main Mission.", "is_course": True, "url": "#"}
    
    # Random selection from Mood Matrix
    if category == "dharma":
        item = random.choice(mood_data['dharma'])
        return {"title": item['title'], "url": item['url'], "is_course": False}
    elif category == "spirit":
        return {"title": random.choice(mood_data['spirit'])}
    elif category == "leela":
        return {"title": random.choice(mood_data['leela'])}

# Initialize Tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = {
        "dharma": get_task("dharma", mode="course"),
        "spirit": get_task("spirit"),
        "leela": get_task("leela")
    }

# --- UI LAYOUT ---
st.title("🦁 Harshit's Reality Protocol")
st.caption(f"Date: {datetime.date.today()} | No Zero Days.")

# 1. MOOD SELECTOR
selected_mood = st.selectbox("Current State:", list(mood_matrix.keys()))

if selected_mood != st.session_state.current_mood:
    st.session_state.current_mood = selected_mood
    # If emergency, force random small tasks. If normal, default to course.
    mode = "random" if "Emergency" in selected_mood else "course"
    st.session_state.tasks['dharma'] = get_task("dharma", mode=mode)
    st.session_state.tasks['spirit'] = get_task("spirit")
    st.session_state.tasks['leela'] = get_task("leela")
    st.rerun()

st.divider()

# 2. THE DASHBOARD
col1, col2, col3 = st.columns(3)

# Dharma
with col1:
    st.subheader("⚔️ Dharma")
    t = st.session_state.tasks['dharma']
    with st.container(border=True):
        st.write(f"**{t['title']}**")
        if t.get('url') and t['url'] != "#":
            st.link_button("🔗 Open", t['url'])
        
        # Only show course logging if NOT in emergency mode
        if t.get('is_course') and "Emergency" not in st.session_state.current_mood:
            if st.button("✅ Log 20m"):
                st.session_state.active_project['hours_done'] += 0.33
                st.balloons()
                st.rerun()
    
    # Shuffle only visible if NOT emergency
    if "Emergency" not in st.session_state.current_mood:
        if st.button("🔄 Swap Task"):
            st.session_state.tasks['dharma'] = get_task("dharma", mode="random")
            st.rerun()

# Spirit
with col2:
    st.subheader("🪷 Spirit")
    t = st.session_state.tasks['spirit']
    with st.container(border=True):
        st.write(f"**{t['title']}**")
    if st.button("🔄 Shuffle Spirit"):
        st.session_state.tasks['spirit'] = get_task("spirit")
        st.rerun()

# Leela
with col3:
    st.subheader("💃 Leela")
    t = st.session_state.tasks['leela']
    with st.container(border=True):
        st.write(f"**{t['title']}**")
    if st.button("🔄 Shuffle Joy"):
        st.session_state.tasks['leela'] = get_task("leela")
        st.rerun()

# 3. THE CEO LOG (Output)
st.divider()
st.subheader("🧠 CEO Daily Log")
journal = st.text_area("One decision, insight, or win from today:", placeholder="I realized that...")

# 4. ACCOUNTABILITY SHARER
if st.button("📋 Generate 'Proof of Work'"):
    report = f"""
    🦁 Harshit's Daily Report ({datetime.date.today()})
    --------------------------------
    ✅ Mood: {st.session_state.current_mood}
    ⚔️ Dharma: {st.session_state.tasks['dharma']['title']}
    🪷 Spirit: {st.session_state.tasks['spirit']['title']}
    💃 Leela: {st.session_state.tasks['leela']['title']}
    🧠 Insight: {journal if journal else 'No entry'}
    --------------------------------
    Status: Won the day.
    """
    st.code(report, language="text")
    st.caption("Copy this and WhatsApp it to your partner or save it in your notes.")

# SIDEBAR
with st.sidebar:
    st.header("🦁 Empire Stats")
    proj = st.session_state.active_project
    st.write(f"**Focus:** {proj['name']}")
    st.progress(min(proj['hours_done'] / proj['total_hours'], 1.0))
    st.caption(f"{int(proj['hours_done'])} / {proj['total_hours']} Hrs")
    
    with st.expander("⚙️ Edit Project"):
        new_name = st.text_input("Name", value=proj['name'])
        new_hours = st.number_input("Goal (Hrs)", value=int(proj['total_hours']))
        if st.button("Save"):
            st.session_state.active_project['name'] = new_name
            st.session_state.active_project['total_hours'] = new_hours
            st.rerun()
