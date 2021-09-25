from twitterapi import get_tweet_info_by_location
from mocktextanalysisapi import mock_get_sentiment
from constants import SENTIMENTS
    
def get_sentiment_by_location(trends):
    ta = []
    for trend in trends:
        key = next(iter(trend))
        value = trend[key]
        sentiments = mock_get_sentiment(value)
        count={s:0 for s in SENTIMENTS}
        for sentiment in sentiments:
            count[sentiment['classifications'][0]['tag_name']] += 1
        ta.append({key:count})
    return ta