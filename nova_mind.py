import importlib

def run_learned_code(module_name, func_name):
    try:
        mod = importlib.import_module(f"knowledge.{module_name}")
        func = getattr(mod, func_name)
        return func()
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    print("Nova Mind is ready.")
    while True:
        cmd = input(">>> ")
        if cmd.lower() in ["exit", "quit"]:
            break
        if cmd.startswith("run "):
            try:
                parts = cmd[4:].split(".")
                if len(parts) == 2:
                    module, func = parts
                    print(run_learned_code(module.strip(), func.strip()))
                else:
                    print("Use format: run module.function")
            except Exception as e:
                print(f"Failed to execute: {e}")
