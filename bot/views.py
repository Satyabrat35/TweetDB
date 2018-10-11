from bot.selfy import TweetDbz
from bot.myjson import jsonresponse
from flask import Flask, request, Response
import json
from bot.db import query, csv_writer

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hola!!! Bienvenido a TweetDB </h1>'

@app.route('/api1')
def apione():
    res = dict()
    try:
        keywords = request.args.get('keywords')
        if keywords:
            keywords = keywords.split(",")
            print(keywords)
        else:
            res = {
                "status": "error",
                "message": "Provide keywords",
                "example": "/api1?keywords=modi,Brexit"
            }
            return jsonresponse(res)
        TweetDbz().filtering(keywords=keywords)
        res['status'] = "success"
        res['message'] = "Stream started with {}".format(keywords)
    except Exception as ex:
        res['status'] = "error"

    return jsonresponse(res)

@app.route('/api2',methods=['GET', 'POST'])
def apitwo():
    try:
        start = int(request.args.get('start'))
        end = int(request.args.get('end'))
        twtext = request.args.get('twtext')
        uname = request.args.get('uname')
        sort_val = request.args.get('sort')
        lang = request.args.get('lang')
        date = request.args.get('date')
        rtct = request.args.get('rtct')
        favct = request.args.get('favct')
        sname = request.args.get('sname')

        lang = lang if lang is not None else ""
        twtext = twtext if twtext is not None else ""
        sname = sname if sname is not None else ""
        uname = uname if uname is not None else ""
        sort_val = sort_val if sort_val is not None else "zero"
        date = date if date is not None else ""
        rtct = rtct if rtct is not None else "zero"
        favct = favct if favct is not None else "zero"

        result = query(twtext,uname,sort_val,end,start,date,favct,rtct,lang,sname)
        res = json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False)
        res = json.loads(res)
        return Response(res, mimetype="application/json")

    except Exception as ex:
        res = dict()
        res['status'] = 'error'
        return jsonresponse(res)

@app.route('/api3', methods=['GET', 'POST'])
def apithree():
    csv_writer()
    result = {
        'Message': 'Success',
        'Result': 'CSV file is present in folder with name script.csv'
    }

    return jsonresponse(result)


