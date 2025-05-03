# nova_brain.py
from nova_memory import load_memory
from nova_log import log_interaction
from nova_learn import run_learned_function
from search_online import search_duckduckgo

class NovaBrain:
    def __init__(self):
        self.memory = load_memory()
        log_interaction("NovaBrain initialized.")

    def decide_action(self, user_input):
        if "search" in user_input:
            result = search_duckduckgo(user_input.replace("search", "").strip())
            log_interaction(f"Search: {user_input}")
            return result
        elif "use" in user_input:
            topic = user_input.replace("use", "").strip()
            return run_learned_function(topic)
        else:
            return "Nova is thinking..."

# Teszteléshez
if __name__ == "__main__":
    brain = NovaBrain()
    while True:
        user_input = input("You (to NovaBrain): ")
        if user_input in ["exit", "quit"]:
            break
        print("Nova:", brain.decide_action(user_input))
