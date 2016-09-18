# -*- coding: utf-8 -*-
import flask
from flask import Flask
from flask import request
from threading import Thread
import Queue
import time

class WorkerServer(object):
    def __init__(self, port, name='Worker'):
        self.port = port
        self.receive_listeners = []
        self.app = Flask(name)
        self.app.add_url_rule('/bulai/<action_name>', None, self.bulai, methods=['POST', 'GET'])
        self.app.add_url_rule('/stop', None, self.stop)

    def start(self):
        Thread(target=self.run_server).start()
        print('Start httpd.')
        time.sleep(3)

    def run_server(self):
        self.app.run(host='0.0.0.0', port=self.port)

    def stop(self):
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
        print ('httpd server shutdown.')
        return "STOP"

    def bulai(self, action_name):
        response = {"name": "Unknown action"}
        if action_name=="can_leave":
            response = {"name": "bulai", "can_leave": True}
        return flask.jsonify(response)