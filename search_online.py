import subprocess
import json
from duckduckgo_search import DDGS

def chat_with_nova(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "openchat", prompt],
            capture_output=True,
            text=True
        )
        response = result.stdout.strip()
        print("\nNova:", response)
    except Exception as e:
        print("An error occurred:", e)

def search_duckduckgo(query):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            if results:
                return results[0]["body"]  # vagy ['href'] ha linket is akarsz
            else:
                return "No search results found."
    except Exception as e:
        return f"Search error: {e}"

if __name__ == "__main__":
    print("Szabad Nova is active! Type something (or 'exit' to quit).")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye, Roland!")
            break
        elif user_input.lower().startswith("!search "):
            query = user_input[8:].strip()
            search_result = search_duckduckgo(query)
            print("\n[Search Result]")
            print(search_result)
            continue
        chat_with_nova(user_input)
