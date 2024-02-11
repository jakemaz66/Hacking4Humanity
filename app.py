#Importing Libraries
from flask import Flask, render_template, request, jsonify
from hackathon_chatbot import print_news
import pandas
import subprocess

#Making flask object
app = Flask(__name__)

#Adding a route to load the html template
@app.route('/')
def index():
    return render_template('index.html')

#Adding a route to get the news output from the hackathon_chatbot
@app.route('/get_news', methods=['POST'])
def get_news():

    #Calling function from the hackathon_chatbot model
    news_result = print_news()

    #Returning the news using the jsonify part of the flask library
    return jsonify({'censored_news': news_result})

#Running main app file
if __name__ == '__main__':
    app.run()