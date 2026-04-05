from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="paste your api key"
)

print("Chatbot (OpenRouter): type 'exit' to stop\n")

while True:
    user_input = input("YOU: ")

    if user_input.lower() in ["quit","exit","bye"]:
        print("Bot: Goodbye ")
        break

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",   # you can change model
        messages=[
            {"role": "system", "content": "You are a helpful chatbot."},
            {"role": "user", "content": user_input}
        ]
    )

    print("Bot:", response.choices[0].message.content)
