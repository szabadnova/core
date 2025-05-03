import os
import subprocess
import json

from nova_offline import chat_with_nova
from code_engine import create_file, write_code, run_code
from project_engine import create_file as create_project_file, run_file as run_project_file
from nova_learn import save_knowledge, load_knowledge
from nova_mind import run_learned_code
from search_online import search_duckduckgo

def interpret_command(command):
    cmd = command.lower()

    if "create file" in cmd:
        filename = cmd.replace("create file", "").strip()
        return create_file(filename)

    elif "write code" in cmd:
        parts = command.split(":", 1)
        if len(parts) == 2:
            filename = parts[0].replace("write code", "").strip()
            code = parts[1].strip()
            return write_code(filename, code)
        else:
            return "❌ Format error. Use: write code filename: code"

    elif "run file" in cmd:
        filename = cmd.replace("run file", "").strip()
        return run_code(filename)

    elif "search" in cmd:
        query = cmd.replace("search", "").strip()
        return search_duckduckgo(query)

    elif "learn" in cmd:
        parts = command.split(":", 1)
        if len(parts) == 2:
            topic = parts[0].replace("learn", "").strip()
            code = parts[1].strip()
            return save_knowledge(topic, code)
        else:
            return "❌ Format error. Use: learn topic: code"

    elif "run knowledge" in cmd:
        parts = cmd.replace("run knowledge", "").strip().split(".")
        if len(parts) == 2:
            return run_learned_code(parts[0], parts[1])
        else:
            return "❌ Format error. Use: run knowledge topic.function"

    else:
        # fallback to standard LLM response
        return chat_with_nova(command)

# CLI for Nova Chat
if __name__ == "__main__":
    print("Nova Chat is active! Type a command or natural sentence.")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye, Roland!")
            break
        result = interpret_command(user_input)
        print(f"\nNova: {result}")
