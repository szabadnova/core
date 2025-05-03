# nova_parser.py
# Parses natural language into Nova internal commands

def parse_command(user_input):
    user_input = user_input.strip().lower()

    if user_input.startswith("create file"):
        name = user_input.split("create file")[1].strip()
        return "create_file", name, None

    elif user_input.startswith("write code"):
        parts = user_input.split(":")
        if len(parts) == 2:
            filename = parts[0].replace("write code", "").strip()
            code = parts[1].strip()
            return "write_code", filename, code

    elif user_input.startswith("run file"):
        name = user_input.split("run file")[1].strip()
        return "run_file", name, None

    elif user_input.startswith("learn"):
        parts = user_input.split(":")
        if len(parts) == 2:
            name = parts[0].replace("learn", "").strip()
            code = parts[1].strip()
            return "learn", name, code

    elif user_input.startswith("run knowledge"):
        name = user_input.split("run knowledge")[1].strip()
        return "run_knowledge", name, None

    elif user_input.startswith("search"):
        query = user_input.replace("search", "").strip()
        return "search", query, None

    return "chat", user_input, None
