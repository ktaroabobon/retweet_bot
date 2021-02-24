import tweepy
from tweepy import StreamListener

import setting

auth = tweepy.OAuthHandler(setting.account_id, setting.api_key)

auth.set_access_token(setting.access_token, setting.access_key)

api = tweepy.API(auth)


class CustomStreamListener(StreamListener):

    def on_status(self, status):
        id = status.id
        try:
            api.retweet(id)
        except Exception as e:
            print(e)


def streaming_retweet():
    custom_stream_listener = CustomStreamListener()
    custom_stream_listener = tweepy.Stream(auth=api.auth, listener=custom_stream_listener)

    custom_stream_listener.filter(track=[setting.key_word])
