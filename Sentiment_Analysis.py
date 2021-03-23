from comprehend_auth import comprehend_authenticate
import json
import xlsxwriter
from os import path
import pandas as pd

def sentiment_analysis(text, language):
    comprehend = comprehend_authenticate() #import the authentication function with aws credentials but can be replaced by:
    #comprehend = boto3.client(service_name='comprehend',
    #                                         aws_access_key_id=< Your Access Key,
    #                                         aws_secret_access_key= <Your Secret kay>)

    response = json.loads((json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode=language), sort_keys=True, indent=4))) # refer to aws documentation:https://docs.aws.amazon.com/comprehend/latest/dg/get-started-api-sentiment.html
    sentiment = response['Sentiment']
    sentiment_score = response['SentimentScore']
    return sentiment, sentiment_score

def language_detect(text):
    comprehend = comprehend_authenticate()
    lang_list = json.loads(json.dumps(comprehend.detect_dominant_language(Text=text), sort_keys=True, indent=4))["Languages"][0]
    return lang_list["LanguageCode"]

def tweet_bulk_analysis(filename, keyword):
    def sentiment_assignment(df,index, text,language):
        sentiment, sentiment_score = sentiment_analysis(text, language)
        df.loc[index,'sentiment'] = sentiment
        df.loc[index,'positive_score'] = sentiment_score['Positive']
        df.loc[index,'negative_score'] = sentiment_score['Negative']
        df.loc[index,'neutral_score'] = sentiment_score['Neutral']
        df.loc[index, 'mixed_score'] = sentiment_score['Mixed']
        return
    df = pd.read_csv(filename)
    supported_languages= ['de','en','es','it','pt','fr','jp','ko','hi','ar','zh','zh-TW' ]
    # print(df.columns)
    for index, row in df.iterrows():
        text = row.tweet
        language = row.language
        if language in supported_languages:# check if language of tweet is supported by aws comprehend
            sentiment_assignment(df,index, text, language)
        else:
            language = language_detect(text)
            if language in supported_languages:
                sentiment_assignment(df,index, text, language)
            else:
                df.drop(index, inplace=True)
                return print("Language not supported, the row has been dropped from dataset")
        df.to_csv(f"tweets_with_sentiments_{keyword}.csv")
    return

def sentiment_summary_to_excel(filename, keyword):

    if path.exists(f"tweets_with_sentiments_{keyword}.csv"):
        df = pd.read_csv(f"tweets_with_sentiments_{keyword}.csv")
    else:
        tweet_bulk_analysis(filename, keyword)
        df = pd.read_csv(f"tweets_with_sentiments_{keyword}.csv")
    workbook = xlsxwriter.Workbook(f'sentiment_analysis_{keyword}_summary.xlsx')
    worksheet = workbook.add_worksheet()
    average_scores = (["Average negative score", df.negative_score.mean()],
                      ["Average positive score", df.positive_score.mean()],
                      ["Average mixed score", df.mixed_score.mean()],
                      ["Average neutral score", df.neutral_score.mean()])
    col =1
    row =0
    worksheet.write(row, col, "Total tweets")
    worksheet.write_number(row, col + 1, len(df.index))
    for title, score in average_scores:
        worksheet.write_string(row+2, col,title)
        worksheet.write_number(row+2, col+1, score)
        row+=1

    workbook.close()
    return print(f"The output of the analysis is saved in the file: sentiment_analysis_{keyword}_summary.xlsx")
