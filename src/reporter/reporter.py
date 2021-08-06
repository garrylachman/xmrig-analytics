from reporter.reporter_send_worker import ReporterSendWorker
from reporter.reporter_event_worker import ReporterEventWorker

from logzero import logger
import threading, queue

class Reporter():
    
    def __init__(self, config, result_queue):
        self.config = config
        self.result_queue = result_queue
        self.jobs_queue = queue.Queue()
                
    def start(self):
        threading.Thread(
            target=ReporterEventWorker,
            args=(self.config.reporter.events, self.result_queue, self.jobs_queue,),
            name='reporter-event-worker',
            daemon=True,
        ).start()
        
        for i in range(self.config.reporter.threads):
            worker = threading.Thread(
                target=ReporterSendWorker,
                args=(self.jobs_queue, self.config),
                name='reporter-send-worker-{}'.format(i),
            )
            worker.setDaemon(True)
            worker.start()
            
