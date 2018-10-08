#-*- coding: utf-8 -*-

import json
import pyexcel
from flask import make_response
import io

def jsonresponse(data=None):
    json_res = None

    if data == None:
        json_res = '{}'
    else:
        json_res = json.dumps(data)

    return json_res

# create a csv method ----


