# nova_chat.py – NLP alapú parancsértelmező

import sys
sys.path.append(".")  # biztos importhoz

from code_engine import create_file, write_code, run_code
from nova_learn import learn_function, run_learned_function
from search_online import search_duckduckgo

def parse_nlp(user_input):
    text = user_input.lower().strip()

    if "create file" in text:
        name = text.split("create file")[1].strip()
        return "create_file", name, None

    if "write code" in text:
        parts = text.split("write code")[1].strip().split(":", 1)
        if len(parts) == 2:
            name = parts[0].strip()
            code = parts[1].strip()
            return "write_code", name, code

    if "run file" in text:
        name = text.split("run file")[1].strip()
        return "run_code", name, None

    if "learn" in text:
        parts = text.split("learn")[1].strip().split(":", 1)
        if len(parts) == 2:
            name = parts[0].strip()
            code = parts[1].strip()
            return "learn_function", name, code

    if "run knowledge" in text:
        name = text.split("run knowledge")[1].strip()
        return "run_learned_function", name, None

    if "search" in text:
        query = text.split("search")[1].strip()
        return "search_duckduckgo", query, None

    return "chat", user_input, None

def chat_loop():
    print("Szabad Nova is active! Talk to me naturally (or type 'exit' to quit).")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Nova: Goodbye, Roland!")
            break

        action, param1, param2 = parse_nlp(user_input)

        if action == "create_file":
            print(create_file(param1))

        elif action == "write_code":
            print(write_code(param1, param2))

        elif action == "run_code":
            print(run_code(param1))

        elif action == "learn_function":
            print(learn_function(param1, param2))

        elif action == "run_learned_function":
            print(run_learned_function(param1))

        elif action == "search_duckduckgo":
            print("\n[Nova Search Result:]")
            print(search_duckduckgo(param1))

        else:
            print("Nova: I'm not sure what you mean yet. Try a valid command.")

if __name__ == "__main__":
    chat_loop()
