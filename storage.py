import json
import os

def save_data(data, filename="expenses.json"):
    with open(filename, "w") as f:
        json.dump(data, f)

def load_data(filename="expenses.json"):
    if not os.path.exists(filename):
        return {}
    with open(filename, "r") as f:
        return json.load(f)