from sys import path
from logzero import logger
import time
import threading
from google_measurement_protocol import report, event, pageview


class ReporterSendWorker():
    
    def __init__(self, queue, config):
        self.config = config
        while True:
            item = queue.get()
            self.send(job=item)
            queue.task_done()
            
    def send(self, job):
        data = pageview(
            path=job['worker'],
            title=job['worker']
        )
        report(self.config.ga.tracking_id, job['worker'], data, extra_headers={"User-Agent": "XMRigAnalitics/0.1"})
        
        data = event(
            category=job['category'], 
            action=job['action'], 
            value=job['value'],
            label=job['value']
        )
        report(self.config.ga.tracking_id, job['worker'], data, extra_headers={"User-Agent": "XMRigAnalitics/0.1"})