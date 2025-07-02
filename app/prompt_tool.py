from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

while True:
    user_input = input("\nEnter your prompt (or type 'exit' to quit): ")
    if user_input.lower() == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )

    print("\n🔹 GPT Response:\n", response.choices[0].message.content)
