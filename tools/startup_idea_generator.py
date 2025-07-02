# ✅ Debug: Start of script
print("Script started...")

from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from dotenv import load_dotenv
import os

# ✅ Load .env file
load_dotenv()

# ✅ Debug: Show loaded token (safe for testing)
print("HuggingFace Token:", os.getenv("HUGGINGFACEHUB_API_TOKEN"))

# ✅ Set up Hugging Face model
llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": 0.5, "max_length": 100}
)

# ✅ Define prompt template
prompt = PromptTemplate(
    input_variables=["field"],
    template="Suggest a creative startup idea in the field of {field}."
)

# ✅ Create LangChain pipeline
chain = LLMChain(llm=llm, prompt=prompt)

# ✅ Take user input
user_input = input("Enter a field (e.g., education, health, travel): ")

# ✅ Run the chain
output = chain.run(user_input)

# ✅ Print result
print("\n💡 Startup Idea:")
print(output)
