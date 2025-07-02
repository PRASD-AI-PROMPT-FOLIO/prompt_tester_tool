import streamlit as st
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

st.set_page_config(page_title="Prompt Tester", layout="centered")

st.markdown("# 🧪 AI Prompt Testing Tool")
st.markdown("Welcome to your personal LLM testing playground. Test prompts, view history, export results.")

# Load prompt history
history_file = "prompt_history.json"
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        prompt_history = json.load(f)
else:
    prompt_history = []

# Sidebar for history
st.sidebar.header("📜 Prompt History")
if prompt_history:
    selected_prompt = st.sidebar.selectbox(
        "Choose a previous prompt:", [item["prompt"] for item in prompt_history]
    )
    if st.sidebar.button("🔄 Load Prompt"):
        st.session_state["prompt"] = selected_prompt
else:
    st.sidebar.info("No prompt history yet.")

# Session memory
if "prompt" not in st.session_state:
    st.session_state["prompt"] = ""
if "chat_messages" not in st.session_state:
    st.session_state.chat_messages = []

# UI Inputs
st.divider()
prompt = st.text_area("✍️ Enter your prompt:", value=st.session_state["prompt"])
model = st.selectbox("🤖 Select a model:", ["gpt-3.5-turbo", "gpt-4"])
temperature = st.slider("🎨 Creativity level (temperature):", 0.0, 1.0, 0.7)
system_role = st.text_input("🎯 System Instruction (optional)", "You are a helpful assistant.")

# Buttons
col1, col2 = st.columns(2)
with col1:
    generate = st.button("🚀 Generate Response")
with col2:
    clear = st.button("🧹 Clear Conversation")

# Generate Response
if generate:
    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:
        st.session_state.chat_messages.append({"role": "user", "content": prompt})
        with st.spinner("Generating..."):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "system", "content": system_role}] + st.session_state.chat_messages,
                    temperature=temperature
                )
                result = response.choices[0].message.content
                st.session_state.chat_messages.append({"role": "assistant", "content": result})

                st.success("✅ AI Response:")
                st.write(result)

                prompt_history.append({"prompt": prompt, "response": result})
                with open(history_file, "w") as f:
                    json.dump(prompt_history, f, indent=4)

            except Exception as e:
                st.error(f"❌ Error: {e}")

# Clear Chat
if clear:
    st.session_state.chat_messages = []
    st.success("🧹 Conversation cleared.")

# Export
if st.session_state.chat_messages:
    st.divider()
    export_format = st.radio("📁 Export format:", ["Markdown (.md)", "Text (.txt)"], horizontal=True)
    file_name = "conversation.md" if export_format.startswith("Markdown") else "conversation.txt"

    content = ""
    for msg in st.session_state.chat_messages:
        role = msg["role"].capitalize()
        content += f"{role}:\n{msg['content']}\n\n"

    st.download_button(
        label=" Download Conversation",
        data=content,
        file_name=file_name,
        mime="text/markdown" if export_format.startswith("Markdown") else "text/plain"
    ) 

# ------------------------ Feedback ------------------------
st.divider()
st.subheader("💬 Feedback")
user_feedback = st.text_area("What do you think about this tool?")

if st.button("Submit Feedback"):
    if user_feedback.strip():
        with open("logs/feedback.txt", "a", encoding="utf-8") as f:
            f.write(user_feedback + "\n---\n")
        st.success("✅ Thanks for your feedback!")
    else:
        st.warning("Please enter some feedback before submitting.")
        
st.divider()
st.markdown(" Built by Prasad | Powered by OpenAI | V1.0")
