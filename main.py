from Sentiment_Analysis import  sentiment_summary_to_excel
from Tweet_scrape import tweet_scrape
from os import path
import os

def main(keyword, max_tweet, date):
    filename = f'tweets_extracted/clean_tweets_{search_keyword}.csv'
    if path.exists(filename):
        print("You already did a sentiment for this keyword, would like to do it again (type Y/N)")
        if input().lower() == 'y':
            tweet_scrape(search_keyword, max_tweet, date)
    else:
        tweet_scrape(search_keyword, max_tweet, date)

    # sentiment_summary_to_excel(filename,keyword)

if __name__ == '__main__':
    search_keyword = input("Enter the keyword for tweets search" + '\n')
    max_tweet = input(" Enter the max tweets you want to extract"+'\n')
    date = input('Enter the start date, if no start date press enter to continue'+ '\n')
    directory = 'tweets_extracted'
    if path.exists (directory):
        main (search_keyword, max_tweet, date)
    else:
        os.mkdir (directory)
        main(search_keyword, max_tweet,date)