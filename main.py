from config import *

from flask import Flask
from flask import json
from flask import request

import boto

app = Flask('lobulus-auriculae')

@app.route('/events', methods=[ 'POST' ])
def post_event():
    print 'post_event.json = {}'.format(request.json)
    teeth(json.dumps(request.json))
    return '{ "status": "got it" }'

def teeth(data='{BAD}'):
    response = kinesis.put_record(STREAM_NAME, data=data, partition_key=PARTITION_KEY)
    print 'teeth.response = {}'.format(response)
    return response
