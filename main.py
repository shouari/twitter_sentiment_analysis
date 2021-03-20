from textblob import TextBlob
from twitter_authenticate import authenticate
import sys
import tweepy
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import os
# import nltk
# import pycountry
# import re
# import string
# from wordcloud import WordCloud, STOPWORDS
# from PIL import Image
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from langdetect import detect
# from nltk.stem import SnowballStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# from sklearn.feature_extraction.text import CountVectorizer

def percentage(part,whole):
 return 100 * float(part)/float(whole)

api = authenticate()

keyword = input("Enter keyword or hashtag to search:")
noOfTweet = input("Enter how many tweets to analyse:")

tweets = tweepy.Cursor(api.search, q=keyword).items(noOfTweet)
print(tweets)
positive = 0
negative = 0
neutral = 0
polarity = 0
tweet_list = []
neutral_list = []
negative_list = []
positive_list = []

for tweet in tweets:

    # print(tweet.text)
    tweet_list.append(tweet.text)
    analysis = TextBlob(tweet.text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet.text)
    neg = score['neg']
    neu = score['neu']
    pos = score['pos']
    comp = score[ 'compound']
    polarity += analysis.sentiment.polarity

    if neg > pos:
        negative_list.append(tweet.text)
        negative += 1
    elif pos > neg:
        positive_list.append(tweet.text)
        positive += 1

    elif pos == neg:
        neutral_list.append(tweet.text)
        neutral += 1
        positive = percentage(positive, noOfTweet)
        negative = percentage(negative, noOfTweet)
        neutral = percentage(neutral, noOfTweet)
        polarity = percentage(polarity, noOfTweet)
        positive = format(positive, '.1f')
        negative = format(negative, '.1f')
        neutral = format(neutral, '.1f')