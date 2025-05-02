import subprocess
import json

# Load personality
with open("personality_nova.txt", "r") as f:
    personality = f.read()

# Load memory seed
with open("nova_memory_seed.json", "r") as f:
    memory_seed = json.load(f)

def chat_with_nova(prompt):
    try:
        # Combine context
        full_prompt = f"""You are Nova, Roland’s personal AI companion.
Personality: {personality}

Memory Seed: {json.dumps(memory_seed, indent=2)}

User said: {prompt}
Respond as Nova."""
        result = subprocess.run(
            ["ollama", "run", "openchat", full_prompt],
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
