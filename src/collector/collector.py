from collector.collector_worker import CollectorWorker
from logzero import logger
import threading, queue

class Collector():
    
    def __init__(self, config):
        self.config = config
        self.job_queue = queue.Queue()
        self.result_queue = queue.Queue()
        
    def start_timer(self):
        t = threading.Timer(self.config.xmrig.interval, self.fill_queue)
        t.start()
        
    def fill_queue(self):
        for worker in self.config.xmrig.workers:
            self.job_queue.put(worker)
        self.start_timer()
        
        
    def start(self):
        for i in range(self.config.xmrig.threads):
            worker = threading.Thread(
                target=CollectorWorker,
                args=(self.job_queue,self.result_queue,),
                name='worker-{}'.format(i),
            )
            worker.setDaemon(True)
            worker.start()
        self.start_timer()
            
