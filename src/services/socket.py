import socketio, threading, os

global conn
conn = socketio.Client()

class Socket():
    @staticmethod
    @conn.event
    def connect():
        print('Connected!')
        conn.emit('join', {
            'nickname': os.environ['redebunda-anticheat-nickname'],
            'codigo': os.environ['redebunda-anticheat-codigo']
        })
        os.environ['redebunda-anticheat-bundaId'] = conn.get_sid()

    def disconnect(self):
        conn.disconnect()
        print('Disconnected!')
    
    def connectSocket(self):
        conn.connect('http://127.0.0.1:5000')
    
