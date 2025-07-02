from openai import OpenAI
from dotenv import load_dotenv
import os

# ✅ Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")

# 🔹 Prompt input
prompt = input("Enter your prompt: ")

# 🔹 Send to OpenAI
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

# 🔹 Print result
print("\nGPT says:", response.choices[0].message.content)

