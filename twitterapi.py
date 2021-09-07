import requests
import os

bearertoken=os.environ.get('BEARERTOKEN')

def bearer_authorization(a):
    a.headers['Authorization']=f'Bearer {bearertoken}'
    return a

def get_trending_hashtags_location(location_id):
    endpoint='https://api.twitter.com/1.1/trends/place.json'
    params={'id':location_id}
    response=requests.get(endpoint,auth=bearer_authorization,params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def get_available_locations():
    endpoint = 'https://api.twitter.com/1.1/trends/available.json'
    response = requests.get(endpoint, auth=bearer_authorization, params={})
    return response.json()