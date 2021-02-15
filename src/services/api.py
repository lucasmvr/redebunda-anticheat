import requests


class Api():
    def __init__(self):
        self.baseUrl = 'http://127.0.0.1:5000'
    
    def sendConfig(self, config):
        result = requests.post(self.baseUrl+'/config', json={'data':config})
        return result.status_code == 200
    