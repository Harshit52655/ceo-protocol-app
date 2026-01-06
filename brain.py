import random
import streamlit as st
from mood_library import mood_matrix  # Importing the data from File 1

# Helper to pick task based on mood
def get_task(category, current_mood, active_project, mode="random"):
    # If mode is 'course', we always return the main project
    if category == "dharma" and mode == "course":
        return {
            "title": f"Continue: {active_project['name']}",
            "desc": "The Main Mission.",
            "type": "Project",
            "is_course": True
        }
    
    # Otherwise, look at the mood matrix
    mood_data = mood_matrix[current_mood]
    
    if category == "dharma":
        item = random.choice(mood_data['ceo_task'])
        return {"title": item['title'], "desc": "CEO Skill", "url": item['url'], "is_course": False}
    elif category == "spirit":
        return {"title": random.choice(mood_data['spirit'])}
    elif category == "leela":
        return {"title": random.choice(mood_data['leela'])}
