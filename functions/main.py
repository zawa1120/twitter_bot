import os
import json
import random

from requests_oauthlib import OAuth1Session

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_key_secret = os.environ.get('CONSUMER_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

URL = 'https://api.twitter.com/1.1/statuses/update.json'

def auth_keys(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    return OAuth1Session(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def main(event, context):
    l1 = ["楽天モバイル紹介コード", "楽天モバイル紹介コード♪", "楽天モバイル紹介コード☆", "楽天モバイル紹介コード！"]
    l2 = ["上記の紹介コードで楽天ポイントが1000pt貰えます", "上記の紹介コードで楽天ポイントが1000pt貰えます♪",
          "上記の紹介コードで楽天ポイントが1000pt貰えます☆", "上記の紹介コードで楽天ポイントが1000pt貰えます！"]

    text = random.choice(l1) + "\n\nJX8hyMeQ9vhi\n\n" + random.choice(l2) + "\n\n#楽天モバイル\n#楽天モバイル紹介コード"

    params = {"status": text}
    twitter = auth_keys(consumer_key, consumer_key_secret, access_token, access_token_secret)
    req = twitter.post(URL, params=params)

    if req.status_code != 200:
        print("Failed. - Responce Status Code : {} - Error Code : {}".format(req.status_code, req.json()))
        raise
