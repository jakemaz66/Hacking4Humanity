#Importing Libraries
from flask import Flask, render_template, request, jsonify
from hackathon_chatbot import print_news
import pandas
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_news', methods=['POST'])
def get_news():
    news_result = print_news()
    return jsonify({'censored_news': news_result})

@app.route('/run_python_file', methods=['POST'])
def run_python_file():
    if request.method == 'POST':
        # Replace 'your_script.py' with the name of your Python file
        subprocess.run(['python', 'app.py'])
        return 'Python file executed successfully!'

if __name__ == '__main__':
    app.run(debug=True)