import socketio, threading

global conn, nick, cod
conn = socketio.Client()
sid = conn.get_sid()

class Socket(threading.Thread):
    def __init__(self):
        super().__init__()
    
    @staticmethod
    @conn.event
    def connect():
        global nick, sid, cod
        print('Connected!')
        conn.emit('join', {'nickname': nick, 'codigo': cod})
        sid = conn.get_sid()
    
    def join(self):
        conn.disconnect()
        print('Disconnected!')
        super().join()
    
    def connectSocket(self, nickname, codigo):
        global nick, cod
        nick = nickname
        cod = codigo
        conn.connect('http://127.0.0.1:5000')
        return conn.sid
    
    def getData(self):
        global sid, nick, cod
        return {
            'bundaId': sid,
            'nickname': nick,
            'codigo': cod
        }
    
