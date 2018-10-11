import pymongo
import pprint
import csv
from bson.json_util import dumps

try:
    print("Connecting ...")
    cluster_uri = "mongodb+srv://analytics:analytics-password@mycluster-zuqqr.mongodb.net/test?retryWrites=true"
    client = pymongo.MongoClient(cluster_uri)
    db = client['test']
    tz = db.tweet
    print("Done :)")
except:
    print("Could'nt Connect")

def convert_csv():
    start_page = 0
    show_page = 30
    betterfilter = {}

    cursor = tz.find(betterfilter).skip(start_page).limit(show_page)
    
    flattened_records = []
    for record in cursor:
        flattened_record = {
            'Username': record['Username'],
            'Device': record['SourceDevice'],
            'Tweet': record['TweetText'],
            'Language': record['Language'],
            'FavouriteCounts': record['FavouriteCount'],
            'ReplyCounts': record['ReplyCount']
        }
        flattened_records.append(flattened_record)
    print(flattened_records)

    with open('script.csv','w') as outfile:
        fields = ['Username', 'Device', 'Tweet', 'Language', 'FavouriteCounts', 'ReplyCounts']
        write = csv.DictWriter(outfile, fieldnames=fields)
        write.writeheader()
        for flattened_record in flattened_records:
            write.writerow(flattened_record)
        

convert_csv()