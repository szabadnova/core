import subprocess

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

if __name__ == "__main__":
    print("Szabad Nova is active! Type something (or 'exit' to quit).")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye, Roland!")
            break
        chat_with_nova(user_input)
