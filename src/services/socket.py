import socketio, threading, os

global conn
conn = socketio.Client()

class Socket(threading.Thread):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    @conn.event
    def connect():
        print('Connected!')
        conn.emit('join', {
            'nickname': os.environ['redebunda-anticheat-nickname'],
            'codigo': os.environ['redebunda-anticheat-codigo']
        })
        os.environ['redebunda-anticheat-bundaId'] = conn.get_sid()
    
    def join(self):
        conn.disconnect()
        print('Disconnected!')
        super().join()
    
    def connectSocket(self):
        conn.connect('http://127.0.0.1:5000')
    
