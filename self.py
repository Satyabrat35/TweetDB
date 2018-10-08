import tweepy
consumer_key = "DwQ8ex1DfR7MXnG3RcGZ9N5YD"
consumer_secret = "SBfSmvwdqj35MkFUmvK3hCGjuhsNnCBE3VKq74WdECkwwxjtAR"
access_token = "1113651799-UtGRf9e2eD0JeC2mXH05IaeBggP5sG3ANNPfd6P"
access_token_secret = "leQwB8GcDatCArnx7OGdqssoZpxdz41YBKcjxptJ8fUnf"


class TweetDb(object):
    def __init__(self, listener = tweepy.StreamListener):
        self.listener = listener
        self.__auth__ = None

    def __authorize__(self):
        if self.__auth__ == None:
            self.__auth__ == tweepy.OAuthHandler(consumer_key, consumer_secret)
            self.__auth__.set_access_token(access_token, access_token_secret)
        return self.__auth__ is not None

    def __streamer__(self):
        authenticated = self.__authorize__()
        if is authenticated:
            return tweepy.Stream(self.__auth__, self.listener)
        return None

    def filter(self, keywords=None):
        sleeptime = 45
        streamer = self.__streamer__()
        try:
            streamer.fliter(track=keywords,async=True)
            time.sleep(sleeptime)
            streamer.disconnect()
            print("Done :)")
        except:
            print(Exception.message)
            

