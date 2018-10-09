import tweepy
import pymongo


try:
    print("Connecting ...")
    cluster_uri = "mongodb+srv://analytics:analytics-password@mycluster-zuqqr.mongodb.net/test?retryWrites=true"
    client = pymongo.MongoClient(cluster_uri)
    db = client['test']
    tz = db.tweet
    print("Done :)")
except:
    print("Could'nt Connect")



class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        print("we are here also")
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
            return True
        except:
            print("noobs :/")
            return False

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