# -*- coding: utf-8 -*-

from Worker import worker_server
import Queue
import requests


class WorkerManager(object):
    def __init__(self, port):
        self.port = port
        self.server = worker_server.WorkerServer(port)

    def start_server(self):
        self.server.start()

    def stop_server(self):
        requests.get("http://127.0.0.1:%s/stop" % self.port)