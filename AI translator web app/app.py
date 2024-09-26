from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)


genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')


SUPPORTED_LANGUAGES = ['igbo', 'hausa', 'yoruba', 'english', 'korean']  

@app.route('/', methods=['GET', 'POST'])
def translate():
    translated_text = ""
    if request.method == 'POST':
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']
        text_to_translate = request.form['text']

      
        if source_lang not in SUPPORTED_LANGUAGES or target_lang not in SUPPORTED_LANGUAGES:
            translated_text = "Unsupported language selected."
        else:
            prompt = f"Translate the following text from {source_lang} to {target_lang}: {text_to_translate}, just display the translation of the word, no further explanation and add the pronounciation."

            try:
                
                response = model.generate_content(prompt)
                translated_text = response.text
            except Exception as e:
                translated_text = f"An error occurred: {str(e)}"

        return render_template('index.html', translated_text=translated_text, source_lang=source_lang, target_lang=target_lang, text=text_to_translate)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
