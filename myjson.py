
import json
from flask import make_response, jsonify, Response
import csv

# create a json response ----
def jsonresponse(data=None):
    json_res = None

    if data == None:
        json_res = '{}'
    else:
        json_res = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)
    
    return Response(json_res, mimetype="application/json")


# create a csv method ----
def convert_csv(flattened_records):
    print("omg kelly")
    with open('script.csv', 'w') as outfile:
        fields = ['Username', 'Device', 'Tweet', 'Language', 'FavouriteCounts', 'ReplyCounts']
        write = csv.DictWriter(outfile, fieldnames=fields)
        write.writeheader()
        for flattened_record in flattened_records:
            write.writerow(flattened_record)

    return True

