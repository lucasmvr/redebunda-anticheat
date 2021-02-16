import requests


class Api():
    def __init__(self):
        self.baseUrl = 'http://127.0.0.1:5000'
    
    def sendConfig(self, data):
        result = requests.post(
            self.baseUrl+'/config',
            json={
                'data': data['config'],
                'nickname': data['nickname'],
                'bundaId': data['bundaId'],
                'codigo': data['codigo']
            })
        return result.status_code == 200
    