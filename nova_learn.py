# nova_learn.py

import os
import sys
import importlib.util

KNOWLEDGE_DIR = "knowledge"

def ensure_knowledge_dir():
    if not os.path.exists(KNOWLEDGE_DIR):
        os.makedirs(KNOWLEDGE_DIR)

def learn_function(name, code):
    ensure_knowledge_dir()
    filepath = os.path.join(KNOWLEDGE_DIR, f"{name}.py")
    with open(filepath, "w") as f:
        f.write(code)
    return f"Knowledge about '{name}' saved."

def run_learned_function(name):
    ensure_knowledge_dir()
    filepath = os.path.join(KNOWLEDGE_DIR, f"{name}.py")
    if not os.path.exists(filepath):
        return f"No knowledge found for '{name}'."

    sys.path.append(os.path.abspath(KNOWLEDGE_DIR))  # biztosítja az importálást

    try:
        module = importlib.import_module(name)
        func = getattr(module, name)
        return func()
    except Exception as e:
        return f"Error running learned function '{name}': {e}"
