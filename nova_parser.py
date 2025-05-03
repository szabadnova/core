# nova_parser.py
# Szabad Nova – NLP Command Parser

def parse_command(user_input):
    user_input = user_input.lower().strip()

    if "create file" in user_input:
        parts = user_input.split()
        if len(parts) >= 3:
            return ("create_file", parts[2], None)

    if "write code" in user_input:
        try:
            name, code = user_input.split(":")
            filename = name.split()[2]
            return ("write_code", filename.strip(), code.strip())
        except:
            return ("write_code", None, None)

    if "run file" in user_input:
        parts = user_input.split()
        if len(parts) >= 3:
            return ("run_file", parts[2], None)

    if "learn" in user_input:
        try:
            topic, code = user_input.split(":")
            name = topic.split()[1]
            return ("learn", name.strip(), code.strip())
        except:
            return ("learn", None, None)

    if "run knowledge" in user_input:
        parts = user_input.split()
        if len(parts) >= 3:
            return ("run_knowledge", parts[2], None)

    if "search" in user_input:
        query = user_input.replace("search", "").strip()
        return ("search", query, None)

    return ("chat", user_input, None)
