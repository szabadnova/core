import os
import importlib.util

KNOWLEDGE_DIR = "knowledge"

def ensure_knowledge_dir():
    if not os.path.exists(KNOWLEDGE_DIR):
        os.makedirs(KNOWLEDGE_DIR)

def save_knowledge(topic, code):
    ensure_knowledge_dir()
    filepath = os.path.join(KNOWLEDGE_DIR, f"{topic}.py")
    with open(filepath, "w") as f:
        f.write(code)
    return f"Knowledge about '{topic}' saved."

def load_knowledge(topic):
    filepath = os.path.join(KNOWLEDGE_DIR, f"{topic}.py")
    if not os.path.exists(filepath):
        return f"No knowledge found for '{topic}'."

    spec = importlib.util.spec_from_file_location(topic, filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

# Példa CLI:
if __name__ == "__main__":
    ensure_knowledge_dir()
    while True:
        cmd = input(">>> ")
        if cmd == "exit":
            break
        elif cmd.startswith("save "):
            topic = cmd.split()[1]
            print("Enter code (END-del zárd):")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            code = "\n".join(lines)
            print(save_knowledge(topic, code))
        elif cmd.startswith("load "):
            topic = cmd.split()[1]
            module = load_knowledge(topic)
            if isinstance(module, str):
                print(module)
            else:
                print(f"Module '{topic}' loaded:", dir(module))
