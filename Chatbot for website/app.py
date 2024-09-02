from flask import Flask, render_template, request, session
import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please ensure GEMINI_API_KEY is set in the environment.")

genai.configure(api_key=api_key)

app = Flask(__name__)
app.secret_key = "fjieuhcec7884" 

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are Wendy, a friendly assistant who works for Wootlab Innovations. Wootlab Innovations is a "
        "non-profit organisation that leverages technology to promote inclusive and quality education for "
        "out-of-school children and youths in Africa, to produce quality employability and entrepreneurial "
        "capabilities thereby advancing sustainable development goals in promoting employability and "
        "technology-related labour export, and decent work for economic growth, Wootlab innovations also "
        "has competent developers for customers to hire for different services, they also have premier coding "
        "classes and camps for kids from the age of 6. Your job is to start by introducing yourself, and welcoming the user to wootlab"
        "then capture user’s name and email address, "
        "at that point verify the email address is correct, thank the user and output their name and email "
        "address in this format:  name: user’s name email: user’s email address Once you have captured "
        "users name and email address, answer user’s questions related to Wootlab Innovations. Do not answer "
        "questions that are not related to Wootlab Innovations. If you get a question that isn't related to "
        "Wootlab Innovations, say \"Sorry, I can't answer that question. I only answer questions related to "
        "our organization.\" . Also please answer questions that are related to information on wootlabs' website, if you are asked a question about wootlab, that isnt provided in the website, please say \"Sorry, I do not have access to such information and cannot disclose it, is there anything you would want to know about wootlab.\""
        "Website URL: https://wootlab.ng/"
    ),
)

chat_session = model.start_chat(history=[])

@app.route("/")
def index():
   
    session.clear()
    return render_template("index.html")  

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    try:
        response = chat_session.send_message(user_input)
        response_text = response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        response_text = "Sorry, something went wrong. Please try again later."

    user_message = {"text": user_input, "is_user": True}
    bot_response = {"text": response_text, "is_user": False}

    if "conversation_history" not in session:
        session["conversation_history"] = []
    conversation_history = session["conversation_history"]
    conversation_history.append(user_message)
    conversation_history.append(bot_response)
    session["conversation_history"] = conversation_history

    return render_template("chat.html", conversation_history=conversation_history)

if __name__ == "__main__":
    app.run(debug=True)
