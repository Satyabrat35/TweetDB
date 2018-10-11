import tweepy
from bot.listen import MyStreamListener
import time
consumer_key = "<consumer-key>"
consumer_secret = "<consumer-secret>"
access_token = "<access-token>"
access_token_secret = "<access-token-secret>"

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
        #print("we are here")
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
