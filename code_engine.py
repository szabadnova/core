import os
import subprocess

BASE_DIR = "projects"

def ensure_project_dir():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

def create_file(filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w") as f:
        f.write("# Created by Nova\n")
    return f"{filename} created."

def write_code(filename, code):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w") as f:
        f.write(code)
    return f"Code written to {filename}."

def run_code(filename):
    path = os.path.join(BASE_DIR, filename)
    try:
        result = subprocess.run(["python3", path], capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error running {filename}: {e}"

def list_files():
    return os.listdir(BASE_DIR)

def delete_file(filename):
    path = os.path.join(BASE_DIR, filename)
    os.remove(path)
    return f"{filename} deleted."

# Optional CLI loop for testing
if __name__ == "__main__":
    ensure_project_dir()
    print("Nova Code Engine ready. Type 'help' or 'exit'.")
    while True:
        cmd = input(">>> ")
        if cmd == "exit":
            break
        elif cmd.startswith("!new "):
            print(create_file(cmd[5:].strip()))
        elif cmd.startswith("!write "):
            fname = cmd[7:].strip()
            print("Enter code (end with 'END'):")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            code = "\n".join(lines)
            print(write_code(fname, code))
        elif cmd.startswith("!run "):
            print(run_code(cmd[5:].strip()))
        elif cmd.startswith("!list"):
            print("\n".join(list_files()))
        elif cmd.startswith("!delete "):
            print(delete_file(cmd[8:].strip()))
        else:
            print("Unknown command.")
