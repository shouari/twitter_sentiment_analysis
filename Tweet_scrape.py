import twint
import pandas as pd
import os
 # refer to Twint documentation for further details ; https://github.com/twintproject/twint

def tweet_scrape(keyword,max_tweet,date):
    search_keyword = keyword
    date= date
    t = twint.Config()
    t.Search = search_keyword
    t.Store_object = True
    t.Limit = max_tweet
    t.Since = date
    t.Store_csv = True
    t.Output = f"./tweets_extracted/tweets_{search_keyword}.csv"
    twint.run.Search(t)
    # selecting only needed columns
    df = pd.read_csv(f"tweets_extracted/tweets_{search_keyword}.csv")
    df_1 = df.drop(['time','user_id','retweet','created_at','mentions','timezone', 'conversation_id','place', 'urls', 'photos','replies_count','retweets_count','likes_count','hashtags','cashtags','link','quote_url','video','thumbnail','near','geo','source','user_rt_id','user_rt','retweet_id','reply_to','retweet_date','translate','trans_src','trans_dest'], axis =1)
    # dropping the tweets with a specific username I did not need
    df_1 = df_1[df_1.username != search_keyword.lower()]
    df_1.to_csv(f'tweets_extracted/clean_tweets_{search_keyword}.csv')
    os.remove(f"tweets_extracted/tweets_{search_keyword}.csv")
    return print('Extraction Done')
