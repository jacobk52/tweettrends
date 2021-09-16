import requests
import os

bearer_token=os.environ.get('TWITTER_API_BEARER_TOKEN')

def bearer_authorization(a):
    a.headers['Authorization']=f'Bearer {bearer_token}'
    return a

def get(endpoint,params):
    response = requests.get(endpoint, params=params, auth=bearer_authorization)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_tweet_info_by_query(query):
    endpoint = 'https://api.twitter.com/2/tweets/search/recent'
    params = {'query':query,'max_results':10}
    response_json = get(endpoint, params)
    return [d['text'] for d in response_json['data']]

def get_trends_by_location(location_id):
    endpoint='https://api.twitter.com/1.1/trends/place.json'
    params={'id':location_id}
    response_json = get(endpoint, params)
    return [h['name']for h in response_json[0]['trends']]

def get_available_locations():
    endpoint = 'https://api.twitter.com/1.1/trends/available.json'
    response_json = get(endpoint,{})
    return [{
        'name':l['name'],
        'location_id':l['woeid'],
        'country':l['country'],
        'country_code':l['countryCode']
    } for l in response_json]

def get_tweet_info_by_location(location_id):
    trends = get_trends_by_location(location_id)
    return [{trend:[i for i in get_tweet_info_by_query(trend)]} for trend in trends]