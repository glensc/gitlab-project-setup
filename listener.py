#!/usr/bin/python
from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/', methods = ['POST'])
def JsonHandler():
    if request.is_json:
        content = request.get_json()
        print "Just got {0} event!".format(content['event_name'])
        return 'OK'
    else:
        return 'OK'
 
app.run(host='0.0.0.0', port= 8888)