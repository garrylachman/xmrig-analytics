from logzero import logger
import time
import threading
import http.client
import json

class CollectorWorker():
    
    def __init__(self, queue, result_queue):
        while True:
            item = queue.get()
            logger.debug("{}: CollectorWorker get Item".format(threading.current_thread().name))
            result_queue.put(self.send(item))
            queue.task_done()
            
    def send(self, worker):
        conn = http.client.HTTPConnection(
            host=worker.hostname,
            port=worker.port
        )
        conn.request("GET", "/2/summary")
        response = conn.getresponse()
        data = response.read()
        json_data = json.loads(data)
        return {"worker": worker.name, "data": json_data}