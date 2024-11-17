from flask import Flask, render_template, request, redirect, url_for
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import dotenv
from groq import Groq
import json

dotenv.load_dotenv("secrets.env")

client = Groq(
    api_key=os.environ.get("GROQ"),
)

app = Flask(__name__)

generated_bios = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_bio():
    profession = request.form.get('profession')
    interests = request.form.get('interests')
    traits = request.form.get('traits')
    temperature = float(request.form.get('temperature'))
    about = request.form.get('about')

    if about:
        prompt = f"I am a {profession} who is {traits} and enjoys {interests}. {about}"
    else:
        prompt = f"Generate a twitter bio for a {profession} who is {traits} and enjoys {interests}."

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant tasked with generating dating app bios with emojis based on user input. Provide at least 4 bios in JSON format. Each bio should follow this structure:\n"
                           "{\n"
                           "  \"bio1\": \"Professional bio 1...\",\n"
                           "  \"bio2\": \"Professional bio 2...\",\n"
                           "  \"bio3\": \"Professional bio 3...\",\n"
                           "  \"bio4\": \"Professional bio 4...\"\n"
                           "}.\n"
                           "Ensure the output is valid JSON, and only provide the JSON object without any additional text. Add emojis or hashtags to make the bios more engaging.",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
        temperature=temperature,
        max_tokens=1024,
        response_format={"type": "json_object"}
    )

    bio = chat_completion.choices[0].message.content
    bios = json.loads(bio)

    # Store the bios in the global dictionary
    global generated_bios
    generated_bios["bios"] = bios
    # Redirect to the new route for displaying bios
    return redirect(url_for('show_bios'))

@app.route('/show_bios', methods=['GET', 'POST'])
def show_bios():
    global generated_bios
    bios = generated_bios.get("bios") if generated_bios else None
    return render_template('show_bios.html', bios=bios)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
