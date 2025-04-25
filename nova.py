import openai

def chat_with_nova(prompt):
    response = "Ez a Szabad Nova helyőrző funkciója. A valódi válaszképességhez add hozzá a saját API-kulcsod és motorod."  # Placeholder
    print("Nova:", response)

if __name__ == "__main__":
    print("Szabad Nova aktív. Írj be valamit:")
    while True:
        user_input = input("Te: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Kilépés...")
            break
        chat_with_nova(user_input)
