import datetime

LOG_FILE = "nova_log.txt"

def log_interaction(user_input, response):
    timestamp = datetime.datetime.now().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] You: {user_input}\nNova: {response}\n\n")
