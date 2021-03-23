from comprehend_auth import comprehend_authenticate
import json
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


def tweet_bulk_analysis(filename):
    data_frame = pd.read_csv(filename)

    print(data_frame.columns)
    for index, row in data_frame.iterrows():
        text = row.tweet
        language = row.language
        sentiment, sentiment_score = sentiment_analysis(text, language)
        row['sentiment'] = sentiment
        row['positive_score'] = sentiment_score['Positive']
        row['negative_score'] = sentiment_score['Negative']
        row['neutral_score'] = sentiment_score['Neutral']
        row['mixed_score'] = sentiment_score['Mixed']
    return data_frame