import os
import requests

bearer_token=os.environ.get('TWITTER_API_BEARER_TOKEN')

def bearer_authorization(a):
    a.headers['Authorization'] = f'Bearer {bearer_token}'
    return a

def get_tweet_stream():
    endpoint = 'https://api.twitter.com/2/tweets/search/stream'
    response = requests.get(endpoint, auth=bearer_authorization, stream=True)
    if response.status_code != 200:
        raise Exception(response.status_code,response.text)
    return response

def get_current_stream_rules():
    endpoint = 'https://api.twitter.com/2/tweets/search/stream/rules'
    response = requests.get(endpoint,auth=bearer_authorization)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def add_stream_rule(rule):
    endpoint = 'https://api.twitter.com/2/tweets/search/stream/rules'
    payload={'add':[rule]}
    response = requests.post(endpoint, auth=bearer_authorization, json=payload)
    if response.status_code != 201:
        raise Exception(response.status_code, response.text)
    return response.json()

def delete_stream_rule_by_rid(rid):
    endpoint = 'https://api.twitter.com/2/tweets/search/stream/rules'
    payload = {'delete':{'ids':[rid]}}
    response = requests.post(endpoint, auth=bearer_authorization, json=payload)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()