from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os

from services.api import Api

global api
class Spy():
    def __init__(self):
        global api
        api = Api()
        self.spy = Observer()
    
    def start(self):
        path = os.environ['redebunda-anticheat-csPath']
        if not os.path.isfile(path+'/cstrike/config.cfg'):
            raise Exception('ERROR_PATH')
        
        self.handler = PatternMatchingEventHandler([path+'/cstrike/config.cfg'], '', True, True)
        self.handler.on_deleted = self.on_deleted
        self.handler.on_modified = lambda x: self.on_modified(x, self)
        
        self.spy.schedule(self.handler, path+'/cstrike')
        self.spy.start()
    
    def stop(self):
        self.spy.join()

    @staticmethod
    def on_deleted(event):
        print(f"what the f**k! Someone deleted {event.src_path}!")

    @staticmethod
    def on_modified(event, spy):
        print('Ora ora, parece que alguem mudou a cfg....')
        with open(event.src_path, 'r') as file:
            payload = {
                'nickname': os.environ['redebunda-anticheat-nickname'],
                'bundaId': os.environ['redebunda-anticheat-bundaId'],
                'codigo': os.environ['redebunda-anticheat-codigo'],
            }
            payload['data'] = file.read()
            api.sendConfig(payload)