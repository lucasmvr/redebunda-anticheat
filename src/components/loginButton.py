import tkinter as tk
from PIL import Image, ImageTk
import socketio, threading

from tkinter import messagebox

# todo send info to server

def click(button, parent):
    if parent.socketStarted:
        return
    try:
        parent.connectText.insert(1.0, 'Conectando com o servidor...')
        parent.connectText.tag_add('center', 1.0, 'end')
        parent.socket.start()
        parent.socketStarted = True
        sid = parent.socket.connectSocket(parent.nickInput.get())
        parent.connectText.delete(1.0, 'end')
        parent.connectText.insert(1.0, 'Conectado!')
        parent.connectText.tag_add('center', 1.0, 'end')
        parent.sidText.insert(1.0, 'Seu Bunda ID é '+sid)
        parent.sidText.tag_add('center', 1.0, 'end')
        button.configure(state=tk.DISABLED)
    except Exception:
        messagebox.showerror('Ops..', 'Ocorreu um erro com a conexão, contate a organização.')
        if parent.socketStarted:
            parent.socket.join()
        parent.socketStarted = False
        parent.connectText.delete(1.0, 'end')
        parent.connectText.insert(1.0, 'Não foi possível se conectar.')
        parent.connectText.tag_add('center', 1.0, 'end')


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
        self.bind('<Button-1>', lambda x: click(self, self.parent))