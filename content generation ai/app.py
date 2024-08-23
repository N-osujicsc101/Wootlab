from flask import Flask, render_template, request
from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

app = Flask(__name__)

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/', methods=['GET', 'POST'])
def generate_content():
    content = ""
    if request.method == 'POST':
        topic = request.form['topic']
        content_type = request.form['content_type']
        
        prompt = f"Write a {content_type} about {topic}."
        
       
        try:
            response = model.generate_content(prompt)
            content = response.text  
        except Exception as e:
            content = f"An error occurred: {str(e)}"
        
        return render_template('index.html', content=content, topic=topic, content_type=content_type)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
