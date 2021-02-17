import requests


class Api():
    def __init__(self):
        self.baseUrl = 'http://127.0.0.1:5000'
    
    def sendConfig(self, data):
        result = requests.post(
            self.baseUrl+'/config',
            json=data)
        return result.status_code == 200
    
    def sendScreenshot(self, data, image):
        result = requests.post(
            self.baseUrl+'/screenshot?nickname={nickname}&bundaId={bundaId}&codigo={codigo}'.format_map(data),
            data=image
        )
        return result.status_code == 200
    