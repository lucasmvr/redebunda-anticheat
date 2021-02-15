import socketio, threading

global conn, nick
conn = socketio.Client()
sid = conn.get_sid()

class Socket(threading.Thread):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    @conn.event
    def connect():
        global nick, sid
        print('Connected!')
        conn.emit('join', {'nickname': nick})
        sid = conn.get_sid()
    
    def join(self):
        conn.disconnect()
        print('Disconnected!')
        super().join()
    
    def connectSocket(self, nickname):
        global nick
        nick = nickname
        conn.connect('http://127.0.0.1:5000')
        print(conn.get_sid())
        return conn.sid
    
    def getSid(self):
        global sid
        return sid
    
