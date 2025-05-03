# nova_parser.py
# Szabad Nova – NLP Command Parser
# Parses natural language input into internal Nova commands

def parse_input(user_input):
    user_input = user_input.lower().strip()

    # NEW FILE
    if "create a file called" in user_input or user_input.startswith("new file"):
        name = user_input.split("called")[-1].strip() if "called" in user_input else user_input.split("file")[-1].strip()
        return f"!new {name}"

    # WRITE FILE
    elif "write code in" in user_input or "write to" in user_input:
        name = user_input.split("in")[-1].strip() if "in" in user_input else user_input.split("to")[-1].strip()
        return f"!write {name}"

    # RUN FILE
    elif "run the file" in user_input or user_input.startswith("run"):
        name = user_input.split("file")[-1].strip() if "file" in user_input else user_input.replace("run", "").strip()
        return f"!run {name}"

    # SEARCH
    elif user_input.startswith("search for"):
        query = user_input.replace("search for", "").strip()
        return f"!search {query}"

    # LEARN FUNCTION
    elif "learn a function" in user_input or user_input.startswith("teach nova"):
        name = user_input.split("called")[-1].strip() if "called" in user_input else "function"
        return f"!learn {name}"

    # GREETINGS
    elif user_input in ["hi", "hello", "hey"]:
        return "Hello Roland! Ready when you are."

    # FALLBACK
    else:
        return "!unknown"
