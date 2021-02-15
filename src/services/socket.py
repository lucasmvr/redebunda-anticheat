import socketio, threading

global conn, nick
conn = socketio.Client()

class Socket(threading.Thread):
    
    def __init__(self):
        super().__init__()
    
    @staticmethod
    @conn.event
    def connect():
        global nick
        print('Connected!')
        conn.emit('join', {'nickname': nick})
    
    def join(self):
        conn.disconnect()
        print('Disconnected!')
        super().join()
    
    def connectSocket(self, nickname):
        global nick
        nick = nickname
        conn.connect('http://127.0.0.1:5000')
        return conn.sid
    
