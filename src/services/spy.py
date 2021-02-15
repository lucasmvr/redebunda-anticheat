from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import os

from services.api import Api

global api
api = Api()
class Spy():
    def __init__(self):
        self.spy = Observer()
        self.api = Api()
    
    def start(self, path):
        if not os.path.isfile(path+'/cstrike/config.cfg'):
            raise Exception('ERROR_PATH')
        
        self.handler = PatternMatchingEventHandler([path+'/cstrike/config.cfg'], '', True, True)
        self.handler.on_deleted = self.on_deleted
        self.handler.on_modified = self.on_modified
        
        self.spy.schedule(self.handler, path+'/cstrike')
        self.spy.start()
    
    def stop(self):
        self.spy.join()

    @staticmethod
    def on_deleted(event):
        print(f"what the f**k! Someone deleted {event.src_path}!")

    @staticmethod
    def on_modified(event):
        print('Ora ora, parece que alguem mudou a cfg....')
        with open(event.src_path, 'r') as file:
            api.sendConfig(file.read())