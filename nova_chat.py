# nova_chat.py

import os
import sys
sys.path.append(".")  # biztos importhoz

from code_engine import create_file, write_code, run_code
from nova_learn import learn_function, run_learned_function
from search_online import search_duckduckgo
from nova_parser import parse_command

def chat_loop():
    print("Szabad Nova is active! Type something (or 'exit' to quit).")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input in ["exit", "quit"]:
            print("Goodbye, Roland!")
            break

        if user_input.startswith("create file "):
            name = user_input.replace("create file ", "").strip()
            print(create_file(name))

        elif user_input.startswith("write code "):
            parts = user_input.replace("write code ", "").split(":", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                code = parts[1].strip()
                print(write_code(name, code))
            else:
                print("Invalid format. Use: write code filename.py: code")

        elif user_input.startswith("run file "):
            name = user_input.replace("run file ", "").strip()
            print(run_code(name))

        elif user_input.startswith("learn "):
            parts = user_input.replace("learn ", "").split(":", 1)
            if len(parts) == 2:
                topic = parts[0].strip()
                code = parts[1].strip()
                print(learn_function(topic, code))
            else:
                print("Invalid format. Use: learn topic: def ...")

        elif user_input.startswith("run knowledge "):
            topic = user_input.replace("run knowledge ", "").strip()
            print(run_learned_function(topic))

        elif user_input.startswith("search "):
            query = user_input.replace("search ", "").strip()
            result = search_duckduckgo(query)
            print("\n[Search Result:]")
            print(result)

        else:
            print("Nova: I’m not sure what you mean yet. Try a command.")

if __name__ == "__main__":
    chat_loop()
