from Sentiment_Analysis import  sentiment_summary_to_excel
from Tweet_scrape import tweet_scrape
from os import path
import streamlit as st
import os

def main(keyword, max_tweet, date):
    filename = f'tweets_extracted/clean_tweets_{search_keyword}.csv'
    if path.exists(filename):
        st.warning("You already did a sentiment for this keyword, would like to do it again")
        continue_button =st.button("Continue")
        if continue_button:
            tweet_scrape(search_keyword, max_tweet, date)
    else:
        tweet_scrape(search_keyword, max_tweet, date)

    sentiment_summary_to_excel(filename,keyword)

if __name__ == '__main__':
    st.title("Twitter Sentiment Analysis")
    search_keyword = st.text_input('Enter the keyword for tweets search')
    max_tweet = st.number_input(" Enter the max tweets you want to extract",min_value=1,max_value=50000, step=1, help='Max tweets is 50 000')
    date = str(st.date_input('Enter the start date, if no start date'))
    directory = 'tweets_extracted'
    proceed_button = st.button('Proceed')
    if proceed_button:

        if path.exists (directory):
            main (search_keyword, max_tweet, date)
        else:
            os.mkdir (directory)
            main(search_keyword, max_tweet,date)
