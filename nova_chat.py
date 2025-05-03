import sys
sys.path.append(".")  # biztos, ami biztos

from nova_parser import parse_input as parse_command
from code_engine import create_file, write_code, run_code
from nova_learn import learn_function, run_learned_function
from search_online import search_duckduckgo

def chat_loop():
    print("Szabad Nova is active! Type something (or 'exit' to quit).")

    while True:
        user_input = input("\nYou: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye, Roland!")
            break

        action, param1, param2 = parse_command(user_input)

        if action == "create_file":
            print(create_file("knowledge", param1))

        elif action == "write_code":
            print(write_code("knowledge", param1, param2))

        elif action == "run_file":
            print(run_code("knowledge", param1))

        elif action == "learn":
            print(learn_function(param1, param2))

        elif action == "run_knowledge":
            print(run_learned_function(param1))

        elif action == "search":
            result = search_duckduckgo(param1)
            print("\n[Search Result:]")
            print(result)

        else:
            print("Nova: I'm not sure what you mean yet. (NLP not recognized)")

if __name__ == "__main__":
    chat_loop()
