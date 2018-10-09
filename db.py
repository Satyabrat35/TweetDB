import pymongo
import pprint

try:
    print("Connecting ...")
    cluster_uri = "mongodb+srv://analytics:analytics-password@mycluster-zuqqr.mongodb.net/test?retryWrites=true"
    client = pymongo.MongoClient(cluster_uri)
    db = client['test']
    tz = db.tweet
    print("Done :)")
except:
    print("Could'nt Connect")


betterfilter = {
	'FavouriteCount' :{
		'$lte': 3
	},
	'TweetText': {
		'$regex': "tell"
	},
	'Name': {
		'$regex': "1975$"
	}
}
movie = list(tz.find(betterfilter))
pprint.pprint(movie)