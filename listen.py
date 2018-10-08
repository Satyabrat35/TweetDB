import tweepy
import pymongo
consumer_key = "DwQ8ex1DfR7MXnG3RcGZ9N5YD"
consumer_secret = "SBfSmvwdqj35MkFUmvK3hCGjuhsNnCBE3VKq74WdECkwwxjtAR"
access_token = "1113651799-UtGRf9e2eD0JeC2mXH05IaeBggP5sG3ANNPfd6P"
access_token_secret = "leQwB8GcDatCArnx7OGdqssoZpxdz41YBKcjxptJ8fUnf"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

try:
    print("Connecting ...")
    cluster_uri = "mongodb+srv://analytics:analytics-password@mycluster-zuqqr.mongodb.net/test?retryWrites=true"
    client = pymongo.MongoClient(cluster_uri)
    db = client['test']
    print("Done :)")
except:
    print("Could'nt Connect")

tz = db.tweet


#pub = api.home_timeline()
#for tweet in pub:
#    print(tweet.text)
class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        tags = []
        for tag in status.entities['hashtags']:
            tags.append(tag['text'])

        if status.place is not None:
            country = status.place.country
            country_code = status.place.country_code
        else:
            country = ""
            country_code = ""
        
        tweet_dict = {
            "Name": status.user.screen_name,
            "Username": status.user.name,
            "Location": status.user.location,
            "SourceDevice": status.source,
            "Retweets": status.retweeted,
            "Country": country,
            "CountryCode": country_code,
            "TweetText": status.text,
            "FavouriteCount": status.favorite_count,
            "Timestamp": status.timestamp_ms,
            "CreatedAt": status.created_at,
            "ReplyCount": status.reply_count,
            "Language": status.lang,
            "HashTags": tags
        }
        try:
            tz.insert_one(tweet_dict).inserted_id
            print('GG')
        except:
            print("noobs :/")

        print(status.text)


    '''
    def on_error(self,status):
        if status == 420:
            print('maximum connections')
            return False
        elif status == 413:
            print('waiting too long')
            return False
        elif status == 406:
            print('parameter invalid')
            return False
        elif status == 403:
            print('foridden')
            return False
        else:
            return True
'''
        

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)

myStream.filter(track=['LFC'], async=True)