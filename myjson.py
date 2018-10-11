
import json
import pyexcel
from flask import make_response, jsonify, Response
import io


def jsonresponse(data=None):
    json_res = None

    if data == None:
        json_res = '{}'
    else:
        json_res = json.dumps(data, sort_keys=True, ensure_ascii=False, indent=4)
    json_res = json.loads(json_res)

    stored = jsonstore(json_res)
    
    return Response(json_res, mimetype="application/json")

# create a json file  ----
def jsonstore(data):
    
    with open('script.txt', 'w') as fi:
        fi.write(data.decode())

    return True

'''
# create a csv method ----
def json_to_csv():
    infile = open('script.json', 'r')
    outfile = open('data.csv', 'w')
    writer = csv.writer(outfile)
    for row in json.loads(infile.read()):
        writer.write(row)

    return True
'''

