import pymongo
import pprint
from bson.json_util import dumps
from bot.myjson import convert_csv

try:
    print("Connecting ...")
    cluster_uri = "<your-mongodb-compass-cluster-uri>"
    client = pymongo.MongoClient(cluster_uri)
    db = client['test']
    tz = db.tweet
    print("Done :)")
except:
    print("Could'nt Connect")

def query(twtext,uname,sort_val,end,start,date,favct,rtct,lang,sname):
	print('we are here')
	if lang == "":
		lang = 'en'
	
	skip_page = start 
	show_page = end - start + 1
	
	valf = fav(favct)
	valr = rect(rtct)
	if valf == "" and valr == "":
		betterfilter = {
			'TweetText': {
				'$regex': twtext
			},
			'Username': {
				'$regex': uname
			},
			'Language': {
				'$eq': lang
			},
			'Name': {
				'$regex': sname
			}
		}
	elif valf!="" and valr == "":
		vf = int(favct[1:])
		betterfilter = {
			'TweetText': {
				'$regex': twtext
			},
			'Username': {
				'$regex': uname
			},
			'Language': {
				'$eq': lang
			},
			'FavouriteCount': {
				valf: vf
			},
			'Timestamp': {
				'$eq': date
			},
			'Name': {
				'$regex': sname
			}
		}
	elif valf == "" and valr!= "":
		vr = int(rtct[1:])
		betterfilter = {
			'TweetText': {
				'$regex': twtext
			},
			'Username': {
				'$regex': uname
			},
			'Language': {
				'$eq': lang
			},
			'ReplyCount': {
				valr: vr
			},
			'Timestamp': {
				'$eq': date
			},
			'Name': {
				'$regex': sname
			}
		}
	else:
		vf = int(favct[1:])
		vr = int(rtct[1:])
		betterfilter = {
			'TweetText': {
				'$regex': twtext
			},
			'Username': {
				'$regex': uname
			},
			'Language': {
				'$eq': lang
			},
			'FavouriteCount': {
				valf: vf
			},
			'ReplyCount': {
				valr: vr
			},
			'Timestamp': {
				'$eq': date
			},
			'Name': {
				'$regex': sname
			}
		}
	sort_val = sorting(sort_val)
	
	res = list(tz.find(betterfilter).skip(skip_page).limit(show_page).sort(sort_val, pymongo.DESCENDING))
	result = dumps(res)

	return result


def fav(favct):
	val = ''
	if favct[0] == 'l':
		val = '$lte'
	elif favct[0] == 'g':
		val = '$gte'
	elif favct[0] == 'e':
		val = '$eq'
	else:
		val = ''
	
	return val


def rect(rtct):
	val = ''
	if rtct[0] == 'l':
		val = '$lte'
	elif rtct[0] == 'g':
		val = '$gte'
	elif rtct[0] == 'e':
		val = '$eq'
	else:
		val = ''
	
	return val

def sorting(sort_val):
	if sort_val == 'favct':
		sort_val = 'FavouriteCount'
	elif sort_val == 'rtct':
		sort_val = 'ReplyCount'
	else:
		sort_val = 'Timestamp'
	
	return sort_val


def csv_writer():
	show_page = 0
	start_page = 30
	betterfilter = {}

	cursor = tz.find(betterfilter).skip(show_page).limit(start_page)

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
	
	convert_csv(flattened_records)

	return True