#The needed installations, also defined in requirements
#!pip install spacy
#!pip install newsapi-python
#!pip install pycountry
#!python -m spacy download en_core_web_lg
#!pip install better_profanity
#!python -m space download en

#Importing Libraries
import spacy
import pandas as pd
import requests
from better_profanity import profanity
import requests

#Loading the Spacy Model, I chose the large english model for this
nlp = spacy.load('en_core_web_lg')

#Defining an empty list to store news stories
news_stories = []

def NewsStories():
    """
    This function returns the top news stories from the BBC using the News API
    """

    parameters_for_api = {
      "source": "bbc-news",
      "sortBy": "top",
      #This is my custom API key from the News API
      "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }

    #Specifying the news API URL
    main_url = " https://newsapi.org/v1/articles"

    #Getting the data from a request
    data = requests.get(main_url, params=parameters_for_api)

    #Storing the data in javascript oriented notation
    bbc_front_page = data.json()

    news_articles_bbc = bbc_front_page["articles"]

    for i in news_articles_bbc:
        news_stories.append(i["title"])

#Building Chatbot

#Setting minimum threshold for request to be like -> filtering out irrelevant requests
min_similarity = 0.5

def news_chatbot(request):
  """
  This function takes in a request for news and returns the top stories from the BBC

  Args:
  request: str -> A request for news in string format
  """
  #Setting a baseline request to compare the user input to, uses the spacy nlp library
  news = nlp("News Articles")
  statement = nlp(request)

  #If request is valid, call API and return top articles
  if (news.similarity(statement)) >= min_similarity:
    NewsStories()

    return news_stories
  else:
     return "Please ask a valid news related-request!"


def print_news(input):
    """
    This function prints the news gathered from the News API

    Args:
    input: str -> The request made to the chatbot
    """
  
    news_chatbot(input)

    #If request is valid
    if (news_stories):
      #Stray bit of hate speech floating online
      news_stories.append('Asian Americans Deserve Shit')

      censored_news_list = [profanity.censor(news) for news in news_stories]
      censored_news = '\n'.join(censored_news_list)
      return censored_news
    
    else:
        return