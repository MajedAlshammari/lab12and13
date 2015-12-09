from flask import Flask, Response, render_template, request
import json
from subprocess import Popen, PIPE
import os
from tempfile import mkdtemp
from werkzeug import secure_filename

import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2


app = Flask(__name__)

@app.route("/")
def index():
    return """
Available API endpoints: \n
GET			 /queues	List	all	queues
POST		 /queues  Create	a	new	queue
DELETE	 /queues/<qid>	 Delete	a	specific	queue
GET			 /queues/<qid>/msgs Get	a	message,	return	it	to	the	user	
GET			 /queues/<qid>/msgs/count Return	the	number	of	messages	in	a	queue
POST		/queues/<qid>/msgs Write	a	new	message	to	a	queue
DELETE		/queues/<qid>/msgs Get and	delete a message	from	the	queue
"""

@app.route("/key" , methods=['GET'])
def	get_conn():
key_id,	secret_access_key	=	urllib2.urlopen("http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key").read().split(':')
return	boto.sqs.connect_to_region("eu-west-1",	aws_access_key_id=key_id,	aws_secret_access_key=secret_access_key)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080,  debug=True)
