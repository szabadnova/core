# nova_learn.py

import os
import importlib.util

KNOWLEDGE_DIR = "knowledge"

def ensure_knowledge_dir():
    if not os.path.exists(KNOWLEDGE_DIR):
        os.makedirs(KNOWLEDGE_DIR)

def learn_function(name, code):
    ensure_knowledge_dir()
    filename = f"{name}.py"
    filepath = os.path.join(KNOWLEDGE_DIR, filename)
    
    with open(filepath, "w") as f:
        f.write(code + "\n")
    
    return f"Knowledge about '{name}' saved to {filepath}"

def run_learned_function(name):
    filepath = os.path.join(KNOWLEDGE_DIR, f"{name}.py")
    if not os.path.exists(filepath):
        return f"No knowledge found for '{name}'."

    spec = importlib.util.spec_from_file_location(name, os.path.abspath(filepath))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    func = getattr(module, name)
    return func()
