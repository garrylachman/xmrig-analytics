from logzero import logger
import json

class ConfigBase():
    def __init__(self, keys):
        self.keys = keys
    
    def assign(self, obj):
        self.data = { key:value for (key,value) in obj.items() if key in self.keys}

            
  
class GAConfig(ConfigBase):
    def __init__(self, obj):
        super().__init__(["tracking_id"])
        self.assign(obj)
        
    @property
    def tracking_id(self):
        return self.data['tracking_id']


class XMRigWorkerConfig(ConfigBase):
    def __init__(self, obj):
        super().__init__(["hostname", "port", "name", "key"])
        self.assign(obj)
        
    @property
    def hostname(self):
        return self.data['hostname']
    
    @property
    def port(self):
        return self.data['port']
    
    @property
    def name(self):
        return self.data['name']
    
    @property
    def key(self):
        return self.data['key']


class XMRigConfig(ConfigBase):
    def __init__(self, obj):
        super().__init__(["interval", "worker_defaults", "workers", "threads"])
        self.assign(obj)
        self.parse_workers()
        
    @property
    def worker_defaults(self):
        return self.data['worker_defaults']
    
    @property
    def workers(self):
        return self.data['workers']
    
    @property
    def interval(self):
        return self.data['interval']
    
    @property
    def threads(self):
        return self.data['threads']
        
    def parse_workers(self):
        self.data['workers'] = list(map(lambda x: XMRigWorkerConfig({**self.worker_defaults, **x}), self.workers))
      

class ReporterEventsConfig(ConfigBase):
    def __init__(self, obj):
        super().__init__(["category", "action", "value"])
        self.assign(obj)
        
    @property
    def category(self):
        return self.data['category']
    
    @property
    def action(self):
        return self.data['action']
    
    @property
    def value(self):
        return self.data['value']
    

class ReporterConfig(ConfigBase):
    def __init__(self, obj):
        super().__init__(["threads", "events"])
        self.assign(obj)
        self.parse_events()
            
    @property
    def events(self):
        return self.data['events']
    
    @property
    def threads(self):
        return self.data['threads']
        
    def parse_events(self):
        self.data['events'] = list(map(lambda x: ReporterEventsConfig(x), self.events))
    
        

class Config():

    def __init__(self, config_file):
        self.data = json.load(config_file)
        logger.debug(self.data)
        self.parse()
        
    def parse(self):
        self.ga = GAConfig(self.data['ga'])
        self.xmrig = XMRigConfig(self.data['xmrig'])
        self.reporter = ReporterConfig(self.data['reporter'])
                
        logger.debug(vars(self.ga))
        logger.debug(vars(self.xmrig))
        
        for worker in self.xmrig.workers:
            logger.debug(vars(worker))
            
        logger.debug(vars(self.reporter))
            
        for event in self.reporter.events:
            logger.debug(vars(event))
        
        