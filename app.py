#Importing Libraries
from flask import Flask, render_template, request, jsonify
from hackathon_chatbot import print_news


#Making flask object
app = Flask(__name__)

#Adding a route to load the html template
@app.route('/')
def index():
    return render_template('index.html')

#Adding a route to get the news output from the hackathon_chatbot
@app.route('/get_news', methods=['POST'])
def get_news():

    #Getting the user input from the submitted form in the HTML file using the requests library
    data = request.get_json()
    userInput = data.get('userInput')
    
    #Calling function from the hackathon_chatbot model with the input passed as the parameter
    news_result = print_news(userInput)

    #Returning the news using the jsonify part of the flask library
    return jsonify({'censored_news': news_result})

#Running main app file
if __name__ == '__main__':
    app.run()