# prompt_tester_v2.py

prompt_log = [
    {
        "prompt": "Write a poem which starts with letter P, up to 30 lines",
        "audience": "Creative",
        "response": "Poetic response using alliteration with P...",
        "clarity": 4,
        "creativity": 5,
        "tone": "Poetic"
    },
    {
        "prompt": "Explain prompt engineering to a 12-year-old",
        "audience": "Child",
        "response": "Imagine you have a robot friend...",
        "clarity": 5,
        "creativity": 4.5,
        "tone": "Playful"
    },
    {
        "prompt": "Explain prompt engineering to a 25-year-old",
        "audience": "Young adult",
        "response": "Prompt engineering is a digital skill...",
        "clarity": 5,
        "creativity": 4.5,
        "tone": "Professional"
    },
    {
        "prompt": "Explain prompt engineering to a senior software engineer",
        "audience": "Technical expert",
        "response": "It's like optimizing an API call...",
        "clarity": 4.5,
        "creativity": 5,
        "tone": "Technical"
    }
]

def display_all_prompts():
    print("\n--- Prompt Testing Results ---")
    for i, entry in enumerate(prompt_log):
        print(f"\nPrompt {i+1}: {entry['prompt']}")
        print(f"→ Audience: {entry['audience']}")
        print(f"→ GPT Reply: {entry['response']}")
        print(f"→ Clarity: {entry['clarity']} | Creativity: {entry['creativity']} | Tone: {entry['tone']}")
        print("-" * 50)
def save_to_txt():
    with open("prompt_results.txt", "w", encoding="utf-8") as file:
        file.write("🧠 Prompt Testing Results Log\n")
        file.write("=" * 40 + "\n\n")
        for i, entry in enumerate(prompt_log):
            file.write(f"Prompt {i+1}: {entry['prompt']}\n")
            file.write(f"→ Audience: {entry['audience']}\n")
            file.write(f"→ GPT Reply: {entry['response']}\n")
            file.write(f"→ Clarity: {entry['clarity']} | Creativity: {entry['creativity']} | Tone: {entry['tone']}\n")
            file.write("-" * 40 + "\n")
    print("\n✅ Results saved to prompt_results.txt")

if __name__ == "__main__":
    print("🎯 Welcome to Prompt Tester v2")
    input("Press Enter to view all prompt evaluations...\n")
    display_all_prompts()

    save_choice = input("\n💾 Do you want to save these results to a text file? (yes/no): ").strip().lower()
    if save_choice in ["yes", "y"]:
        save_to_txt()
    else:
        print("No problem. File not saved.")
