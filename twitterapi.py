import requests
import os

bearertoken=os.environ.get('BEARERTOKEN')

def bearer_authorization(a):
    a.headers['Authorization']=f'Bearer {bearertoken}'
    return a

def get_tweet_info_by_query(query):
    endpoint = 'https://api.twitter.com/2/tweets/search/recent'
    params = {'query':query,'max_results':10}
    response = requests.get(endpoint, auth=bearer_authorization, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response_json = response.json()
    return [d['text'] for d in response_json['data']]

def get_trends_by_location(location_id):
    endpoint='https://api.twitter.com/1.1/trends/place.json'
    params={'id':location_id}
    response=requests.get(endpoint,auth=bearer_authorization,params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response_json = response.json()
    return [h['name']for h in response_json[0]['trends']][:3]

def get_available_locations():
    endpoint = 'https://api.twitter.com/1.1/trends/available.json'
    response = requests.get(endpoint, auth=bearer_authorization, params={})
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    response_json = response.json()
    return [{
        'name':l['name'],
        'location_id':l['woeid'],
        'country':l['country'],
        'country_code':l['countryCode']
    } for l in response_json]

def get_tweet_info_by_location(location_id):
    trends = get_trends_by_location(location_id)
    return [{trend:[i for i in get_tweet_info_by_query(trend)]} for trend in trends]