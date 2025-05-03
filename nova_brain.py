from nova_memory import load_memory
from nova_log import log_interaction

class NovaBrain:
    def __init__(self):
        self.memory = load_memory()

    def decide_action(self, prompt):
        prompt_lower = prompt.lower()

        if "who is roland" in prompt_lower:
            response = "Roland is my creator and companion. He likes to swim and build intelligent systems like me."
            log_interaction("Nova", response)
            return response

        elif "memory: show" in prompt_lower:
            response = str(self.memory)
            log_interaction("Nova", "[Memory Shown]")
            return response

        elif "run knowledge greet" in prompt_lower:
            try:
                from greet import hi
                result = hi()
                log_interaction("Nova", result)
                return result
            except Exception as e:
                error = f"Error running learned function: {e}"
                log_interaction("Nova", error)
                return error

        elif "thinking" in prompt_lower:
            return "I'm thinking about your request, Roland..."

        else:
            response = "I'm not sure how to respond yet, but I'm learning!"
            log_interaction("Nova", response)
            return response
            if __name__ == "__main__":
    brain = NovaBrain()
    while True:
        user_input = input("You (to NovaBrain): ")
        if user_input.lower() in ["exit", "quit"]:
            print("Nova: Goodbye, Roland.")
            break
        response = brain.decide_action(user_input)
        print(f"Nova: {response}")

