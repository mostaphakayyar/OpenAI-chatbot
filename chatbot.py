import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
conversation_history = []


def chat(user_message):
    conversation_history.append({
        "role" : "user",
        "content" : user_message
    })

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        max_tokens = 1024,
        messages = conversation_history
    )

    assistant_message = response.choices[0].message.content

    conversation_history.append({
        "role" : "assistant",
        "content" : assistant_message
    })

    return assistant_message


def main():
    print("chatbot is ready! Type 'quit' to Exit")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("GoodBye!")
            break
        if user_input.strip() == "":
            continue

        response = chat(user_input)
        print(f"OpenAI: {response}")
        print()

if __name__ == "__main__":
    main()