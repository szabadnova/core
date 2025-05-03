# nova_parser.py
# Szabad Nova – Natural Command Parser

def parse_command(user_input):
    user_input = user_input.lower().strip()

    if user_input.startswith("create file"):
        filename = user_input.replace("create file", "").strip()
        return "create_file", filename, None

    elif user_input.startswith("write code"):
        parts = user_input.split(":", 1)
        if len(parts) == 2:
            filename = parts[0].replace("write code", "").strip()
            code = parts[1].strip()
            return "write_code", filename, code

    elif user_input.startswith("run file"):
        filename = user_input.replace("run file", "").strip()
        return "run_file", filename, None

    elif user_input.startswith("learn"):
        parts = user_input.split(":", 1)
        if len(parts) == 2:
            name = parts[0].replace("learn", "").strip()
            code = parts[1].strip()
            return "learn", name, code

    elif user_input.startswith("run knowledge"):
        name = user_input.replace("run knowledge", "").strip()
        return "run_knowledge", name, None

    elif user_input.startswith("search"):
        query = user_input.replace("search", "").strip()
        return "search", query, None

    return "unknown", user_input, None
