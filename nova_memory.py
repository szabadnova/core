import json
import os

MEMORY_FILE = "nova_memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def remember(key, value):
    memory = load_memory()
    memory[key] = value
    save_memory(memory)
    return f"OK, I’ll remember that."

def recall(key):
    memory = load_memory()
    return memory.get(key, "I don’t remember that.")
