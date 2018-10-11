import tweepy
from listen import MyStreamListener
import time
consumer_key = "DwQ8ex1DfR7MXnG3RcGZ9N5YD"
consumer_secret = "SBfSmvwdqj35MkFUmvK3hCGjuhsNnCBE3VKq74WdECkwwxjtAR"
access_token = "1113651799-UtGRf9e2eD0JeC2mXH05IaeBggP5sG3ANNPfd6P"
access_token_secret = "leQwB8GcDatCArnx7OGdqssoZpxdz41YBKcjxptJ8fUnf"

try:
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    if auth is not None:
        print("Authorized")
    else:
        print("Access Denied")
except:
    print("error in authentication")

class TweetDbz(object):
    def filtering(self, keywords):
        print("we are here")
        sleeptime = 30
        listener = MyStreamListener()
        streamer = tweepy.Stream(auth=auth, listener=listener)
        try:
            streamer.filter(track=keywords,async=True)
            time.sleep(sleeptime)
            streamer.disconnect()
            print("Streamed...")
        except:
            print("Streaming error")
