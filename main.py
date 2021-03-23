from twitter_authenticate import authenticate
import csv
import tweepy
import time
import pandas as pd
import GetOldTweets3 as got

api = authenticate()

text_querry = "GoRafeeq"
retweet_filter='exclude:retweets'
querry = text_querry
count=11000
try:

    tweets = tweepy.Cursor(api.search, q=querry, tweet_mode='extended', since="2021-01-01").items(count)
    #         if tweet.user.screen_name != 'GoRafeeq' and tweet.user.screen_name!= 'khalid1981s':
    tweets_list = [[tweet.created_at, tweet.user.screen_name, tweet.full_text] for tweet in tweets]
    tweets_df = pd.DataFrame(tweets_list)
    tweets_df.to_csv('tweets_extracted.csv')
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)

# print
#
# with open('tweets_extracted.csv','w',newline='', encoding='utf8') as file:
#     fieldnames = ["tweet_created", 'user_name', 'tweet']
#     csvWriter = csv.DictWriter(file, fieldnames=fieldnames)
#     csvWriter.writeheader()
#
#     results = api.search(q=querry, tweet_mode='extended', count=count)
#     for tweet in results:
#         if tweet.user.screen_name != 'GoRafeeq' and tweet.user.screen_name!= 'khalid1981s':
#             # print(tweet.user.screen_name, " Tweeted", tweet.text)
#             csvWriter.writerow({"tweet_created":tweet.created_at,'user_name': tweet.user.screen_name, 'tweet':tweet.full_text})
