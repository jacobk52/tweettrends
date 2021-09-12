from twitterapi import get_tweet_info_by_location
from textanalysisapi import get_sentiment
from constants import SENTIMENTS

def get_sentiment_by_location(location_id):
    trends = get_tweet_info_by_location(location_id)
    ta = []
    for trend in trends:
        key = next(iter(trend))
        value = trend[key]
        sentiments = get_sentiment(value)
        count={s:0 for s in SENTIMENTS}
        for s in sentiments:
            count[s['classifications'][0]['tag_name']]+=1
        ta.append({key:count})
    return ta