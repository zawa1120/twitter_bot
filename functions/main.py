import json
import os
import base64

import tweepy

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_key_secret = os.environ.get('CONSUMER_KEY_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

def auth_keys(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
    return auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def main(event, context):
    '''Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    '''

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    if pubsub_message:
        text = pubsub_message

    else:
        text = "楽天紹介コード\\JX8hyMeQ9vhi\\お互いポイント貰えます♪"

    api = auth_keys(consumer_key, consumer_key_secret, access_token, access_token_secret)
    api.update_status(text)
