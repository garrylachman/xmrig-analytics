from logzero import logger
import time
import threading

class ReporterEventWorker():
    
    def __init__(self, events, queue, jobs_queue):
        while True:
            item = queue.get()
            for event in events:
                job = {
                        "category": event.category,
                        "action": event.action,
                        "worker": item['worker']
                }
                if event.value == "hashrate-10s":
                    job = { **job, "value": item['data']['hashrate']['total'][0] }
                if event.value == "hashrate-60s":
                    job = { **job, "value": item['data']['hashrate']['total'][1] }
                if event.value == "hashrate-15m":
                    job = { **job, "value": item['data']['hashrate']['total'][2] }
                if event.value == "diff_current":
                    job = { **job, "value": item['data']['results']['diff_current'] }
                if event.value == "shares_good":
                    job = { **job, "value": item['data']['results']['shares_good'] }
                if event.value == "shares_total":
                    job = { **job, "value": item['data']['results']['shares_total'] }
                if event.value == "hashes_total":
                    job = { **job, "value": item['data']['results']['hashes_total'] }
                logger.debug(job)
                jobs_queue.put(job)
            
            queue.task_done()