from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class Spy():
    @staticmethod
    def on_deleted(event):
        print(f"what the f**k! Someone deleted {event.src_path}!")

    @staticmethod
    def on_modified(event):
        print('Ora ora, parece que alguem mudou a cfg....')
        with open(event.src_path, 'r') as file:
            line = file.readline()
            while line != '':
                if 'MWHEEL' in line:
                    print(line[:-1])
                line = file.readline()

    def __init__(self):
        patterns = '*'
        ignorePatterns = ''
        ignoreDirectories = True
        caseSensitive = True
        self.handler = PatternMatchingEventHandler(patterns, ignorePatterns, ignoreDirectories, caseSensitive)
        self.handler.on_deleted = self.on_deleted
        self.handler.on_modified = self.on_modified
        self.spy = Observer()
        self.spy.schedule(self.handler, 'teste/doidera/')
    
    def start(self):
        self.spy.start()
    
    def stop(self):
        self.spy.join()
    
    