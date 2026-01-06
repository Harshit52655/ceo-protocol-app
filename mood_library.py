# mood_library.py
# This file contains the raw data (The Mood Matrix)

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
