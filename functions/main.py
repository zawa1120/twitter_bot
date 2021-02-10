import os
import json

from requests_oauthlib import OAuth1Session

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_key_secret = os.environ.get('CONSUMER_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

URL = 'https://api.twitter.com/1.1/statuses/update.json'

def auth_keys(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    return OAuth1Session(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def main(event, context):
    text = "楽天モバイル紹介コード\n\nJX8hyMeQ9vhi\n\n楽天ポイントが1000pt貰えます♪\n\n#楽天モバイル\n#楽天モバイル紹介コード"

    params = {"status": text}
    try:
        twitter = auth_keys(consumer_key, consumer_key_secret, access_token, access_token_secret)
        twitter.post(URL, params=params)

    except Exception as e:
        print(e)
