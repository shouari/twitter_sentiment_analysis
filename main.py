from Sentiment_Analysis import  sentiment_summary_to_excel
from Tweet_scrape import tweet_scrape

def main(keyword):
    filename = f'./tweets_extracted/clean_tweets_{search_keyword}.csv'
    if filename:
        print("You already did a sentiment for this keyword, would like to do it again (type Y/N)"+"\n")
        if input().lower() == 'y':
            tweet_scrape(search_keyword)
    else:
        tweet_scrape(search_keyword)

    sentiment_summary_to_excel(filename,keyword)



if __name__ == '__main__':
    search_keyword = input("Enter the keyword for tweets search" + '\n')
    main(search_keyword)
