from selfy1 import TweetDbz
from myjson import jsonresponse
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Vamos </h1>'

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
                "example": "/api1?keywords=lfc,uefa,ucl"
            }
            return jsonresponse(res)
        TweetDbz().filtering(keywords=keywords)
        res['status'] = "success"
        res['message'] = "Stream started with {}".format(keywords)
    except Exception as ex:
        res['status'] = "error"
        #res['message'] = ex.message
        #res['arguments'] = ex.args

    return jsonresponse(res)

if __name__ == "__main__":
    app.run(debug=True)