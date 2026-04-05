from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# ✅ Put your NEW API key here
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="paste your api key"
)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"reply": "Please enter a message"})

        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # ✅ stable model
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": user_message}
            ]
        )

        bot_reply = response.choices[0].message.content

        return jsonify({"reply": bot_reply})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"reply": "Error: check API or internet"})


if __name__ == "__main__":
    app.run(debug=True)
