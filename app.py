import streamlit as st
import datetime
import json
import random
from openai import OpenAI

# --- CONFIGURATION ---
st.set_page_config(page_title="Harshit's Raj Guru", page_icon="🪔", layout="wide")

# --- 1. THE MASTER INGREDIENTS LIST ---
# This includes EVERYTHING: CEO skills, Python, Spirituality, Family, Dancing, and Socializing.
user_profile = {
    # PILLAR 1: DHARMA (Duty, Ambition, & Leverage)
    # The work you do to build your empire and skills.
    "dharma_career": [
        "Python: Data Structures & Logic Practice",
        "Financial Literacy: Read P&L / Unit Economics article",
        "System Design: Plan how to delegate one personal task",
        "Public Speaking: Watch 1 TEDx talk & analyze the delivery",
        "CEO Challenge: 'The Ask' (Negotiate a bill or ask for a discount)",
        "Strategy: Read 5 pages of 'High Output Management'"
    ],
    
    # PILLAR 2: SPIRIT & ROOTS (God, Family, & Grounding)
    # The connection to the Divine and your loved ones.
    "spirit_roots": [
        "Prayer / Chanting (5 mins connection with God)",
        "Family: Call Parents and listen to their stories",
        "Relationship: Plan a thoughtful date or gesture",
        "Silence: 10 mins of meditation (No phone)",
        "Service: Research a social cause to support"
    ],
    
    # PILLAR 3: LEELA (Divine Play, Joy, & Energy)
    # Lightness of being. Dancing, moving, laughing.
    "leela_joy": [
        "Dance Flow: Put on music and move for 10 mins",
        "Swimming / Physical Play (Summer)",
        "Social: Text a friend to meet up",
        "Cooking: Make a quick meal from scratch",
        "Cinema: Watch a classic movie trailer",
        "Reading: Tech Trends or Light Fiction"
    ],
    
    "max_time": "45 minutes"
}

# --- SESSION STATE ---
if 'daily_plan' not in st.session_state:
    st.session_state.daily_plan = None
if 'karma_score' not in st.session_state:
    st.session_state.karma_score = 0

# --- THE AI RAJ GURU (The Brain) ---
def get_daily_guidance():
    api_key = st.secrets.get("OPENAI_API_KEY")
    
    # FALLBACK (Offline Mode - if no Key found)
    if not api_key:
        return {
            "dharma": {"task": "Python: 2D Arrays", "time": "20 mins", "reason": "Logic building."},
            "spirit": {"task": "Call Mom & Dad", "time": "15 mins", "reason": "Roots matter."},
            "leela": {"task": "Dance to 2 songs", "time": "10 mins", "reason": "Shake off the stress."},
            "message": "Offline Mode: The path is simple today."
        }

    client = OpenAI(api_key=api_key)
    
    # We ask the AI to be your wise Royal Mentor
    prompt = f"""
    Act as a wise 'Raj Guru' (Royal Mentor) for Harshit, a future CEO (age 30).
    Create a 'Daily Path' that balances Ambition (Dharma), Connection (Spirit), and Joy (Leela).
    
    Total Time Budget: STRICTLY {user_profile['max_time']}.
    
    INSTRUCTIONS:
    1. DHARMA (20m): Pick ONE from {user_profile['dharma_career']}.
       - Focus on the 'CEO Gap' (Strategy/Finance) OR 'Builder Skill' (Python).
       
    2. SPIRIT (15m): Pick ONE from {user_profile['spirit_roots']}.
       - This is non-negotiable grounding. God, Family, or Inner Peace.
       
    3. LEELA (10m): Pick ONE from {user_profile['leela_joy']}.
       - Ensure he moves his body or laughs. No stress here.
       
    TONE:
    - Wise, calm, and slightly majestic.
    - No "Hustle" language. Use words like "Cultivate," "Honor," "Flow."
    
    Output purely strictly valid JSON:
    {{
      "dharma": {{"task": "...", "time": "...", "reason": "..."}},
      "spirit": {{"task": "...", "time": "...", "reason": "..."}},
      "leela": {{"task": "...", "time": "..."}},
      "message": "A short wisdom quote for the day"
    }}
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.9, # High variety
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        st.error(f"The Guru is meditating (Error): {e}")
        return None

# --- UI LAYOUT ---
st.title("🪔 Harshit's Life Protocol")
st.caption(f"CEO Ambition • Spiritual Roots • joyful Living | Target: {user_profile['max_time']}/day")

# ACTION BUTTON
if st.button("✨ Seek Today's Guidance"):
    with st.spinner("Consulting the stars..."):
        st.session_state.daily_plan = get_daily_guidance()
        st.rerun()

# DISPLAY THE PATH
if st.session_state.daily_plan:
    plan = st.session_state.daily_plan
    
    # The Guru's Message
    st.info(f"**Guru's Wisdom:** {plan.get('message', 'Balance is power.')}")
    
    # Three Columns for Three Pillars
    c1, c2, c3 = st.columns([1, 1, 1])
    
    # 1. DHARMA
    with c1:
        st.subheader("🦁 Dharma (Duty)")
        with st.container(border=True):
            st.markdown(f"### {plan['dharma']['task']}")
            st.caption(f"⏱️ {plan['dharma']['time']}")
            st.write(f"_{plan['dharma']['reason']}_")
            if st.button("Duty Fulfilled"):
                st.balloons()
                st.session_state.karma_score += 1

    # 2. SPIRIT
    with c2:
        st.subheader("🪷 Spirit (Roots)")
        with st.container(border=True):
            st.markdown(f"### {plan['spirit']['task']}")
            st.caption(f"⏱️ {plan['spirit']['time']}")
            st.write(f"_{plan['spirit']['reason']}_")
            if st.button("Connected"):
                st.success("Peace.")
                st.session_state.karma_score += 1

    # 3. LEELA
    with c3:
        st.subheader("💃 Leela (Play)")
        with st.container(border=True):
            st.markdown(f"### {plan['leela']['task']}")
            st.caption(f"⏱️ {plan['leela']['time']}")
            st.write("Enjoy the flow.")
            if st.button("Joy Felt"):
                st.write("✨")

    # Shuffle Option
    st.divider()
    if st.button("🔄 This path doesn't align today. Shuffle."):
        st.session_state.daily_plan = None
        st.rerun()

# SIDEBAR STATS
with st.sidebar:
    st.header(f"🕉️ Karma Score: {st.session_state.karma_score}")
    st.caption("Days you showed up for yourself.")
    st.divider()
    st.write("**Your Current Ingredients:**")
    with st.expander("See Dharma List"):
        st.write(user_profile['dharma_career'])
    with st.expander("See Spirit List"):
        st.write(user_profile['spirit_roots'])
    with st.expander("See Leela List"):
        st.write(user_profile['leela_joy'])
