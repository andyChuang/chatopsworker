# -*- coding: utf-8 -*-
import sys

sys.path.append('../')

from Worker import WorkerManager
from Worker import config

if __name__ == '__main__':
    worker_server = WorkerManager(config.MOCK_PORT)
    worker_server.start_server()