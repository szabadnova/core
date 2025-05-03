import os
import subprocess

BASE_DIR = "projects"

def ensure_project_dir(project):
    path = os.path.join(BASE_DIR, project)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def create_file(project, filename, content=""):
    path = ensure_project_dir(project)
    file_path = os.path.join(path, filename)
    with open(file_path, "w") as f:
        f.write(content)
    return f"File {filename} created in project {project}."

def read_file(project, filename):
    path = os.path.join(BASE_DIR, project, filename)
    if not os.path.exists(path):
        return f"File {filename} not found in project {project}."
    with open(path, "r") as f:
        return f.read()

def run_file(project, filename):
    path = os.path.join(BASE_DIR, project, filename)
    if not os.path.exists(path):
        return f"File {filename} not found in project {project}."
    try:
        result = subprocess.run(["python3", path], capture_output=True, text=True)
        return result.stdout or result.stderr
    except Exception as e:
        return f"Error running {filename}: {e}"

def list_files(project):
    path = os.path.join(BASE_DIR, project)
    if not os.path.exists(path):
        return f"Project {project} not found."
    return os.listdir(path)

def delete_file(project, filename):
    path = os.path.join(BASE_DIR, project, filename)
    if os.path.exists(path):
        os.remove(path)
        return f"Deleted {filename} from {project}."
    else:
        return f"File not found: {filename}"

# CLI loop
if __name__ == "__main__":
    print("Nova Project Engine ready. Use: !newproj, !addfile, !runfile, !list, !read, !delete, !exit")
    while True:
        cmd = input(">>> ")
        if cmd.lower() == "!exit":
            print("Exiting Project Engine.")
            break
        elif cmd.startswith("!newproj "):
            project = cmd[9:].strip()
            ensure_project_dir(project)
            print(f"Project {project} created.")
        elif cmd.startswith("!addfile "):
            try:
                parts = cmd[9:].strip().split(" ")
                project, filename = parts[0], parts[1]
                print("Enter content, end with END:")
                lines = []
                while True:
                    line = input()
                    if line.strip() == "END":
                        break
                    lines.append(line)
                content = "\n".join(lines)
                print(create_file(project, filename, content))
            except Exception as e:
                print("Error creating file:", e)
        elif cmd.startswith("!runfile "):
            parts = cmd[9:].strip().split(" ")
            if len(parts) == 2:
                print(run_file(parts[0], parts[1]))
        elif cmd.startswith("!read "):
            parts = cmd[6:].strip().split(" ")
            if len(parts) == 2:
                print(read_file(parts[0], parts[1]))
        elif cmd.startswith("!list "):
            project = cmd[6:].strip()
            print("\n".join(list_files(project)))
        elif cmd.startswith("!delete "):
            parts = cmd[8:].strip().split(" ")
            if len(parts) == 2:
                print(delete_file(parts[0], parts[1]))
        else:
            print("Unknown command.")
