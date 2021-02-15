import tkinter as tk
from PIL import Image, ImageTk
import socketio, threading

# todo send info to server

def click(event, parent):
    parent.socket.start()
    parent.socketStarted = True
    parent.socket.teste(parent.nickInput.get())


class LoginButton(tk.Button):
    def __init__(self, root, *args, **kwargs):
        tk.Button.__init__(
            self,
            root,
            text='Entrar',
            highlightcolor='#000',
            activeforeground='#AA1',
            pady=5,
            padx=5,
            *args,
            **kwargs
        )
        self.parent = root
        self.bind('<Button-1>', lambda x: click(x, self.parent))