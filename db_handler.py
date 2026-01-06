import json
import os

DB_FILE = "database.json"

# Default data if no database exists
DEFAULT_DATA = {
    "name": "Python (Boss Coder)",
    "hours_done": 12.0,
    "total_hours": 60
}

def load_data():
    """Check if database exists, if not create it. Return the data."""
    if not os.path.exists(DB_FILE):
        save_data(DEFAULT_DATA)
        return DEFAULT_DATA
    
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return DEFAULT_DATA

def save_data(data):
    """Save the current project state to the file."""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
