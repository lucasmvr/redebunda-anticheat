import tkinter as tk
from PIL import Image, ImageTk
import socketio, threading

from tkinter import messagebox

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
        self.bind('<Button-1>', self.click)
    
    # todo send info to server
    def click(self, event):
        if self.cget('state') == tk.DISABLED: return

        if not self.parent.nickInput.get() or self.parent.nickInput.get().split(' ')[0] == '':
            messagebox.showinfo('Calma lá!', 'Você ainda não digitou seu nickname! (:')
            return

        if not self.parent.pathDescriptor.cget('text'):
            messagebox.showinfo('Calma lá!', 'Você precisa selecionar a pasta de instalação do jogo. (:')
            return
        
        try:
            self.parent.spy.start()
        except Exception:
            messagebox.showerror('Ops...', 'Ocorreu um erro na inicialização do módulo de monitoramento.')
            return

        try:
            self.parent.socket.start()
            self.parent.socketStarted = True
            self.parent.socket.connectSocket(self.parent.nickInput.get())
        except Exception:
            messagebox.showerror('Ops...', 'Ocorreu um erro ao se conectar com o servidor.')
            if self.parent.socketStarted:
                self.parent.socket.join()
                self.parent.spy.stop()
            self.parent.socketStarted = False
            self.parent.connectText.insert(1.0, 'Não foi possível se conectar.')
            self.parent.connectText.tag_add('center', 1.0, 'end')
            return

        self.parent.connectText.insert(1.0, 'Conectado com o servidor!')
        self.parent.connectText.tag_add('center', 1.0, 'end')
        self.parent.spyText.insert(1.0, 'Você está sendo monitorado xD')
        self.parent.spyText.tag_add('center', 1.0, 'end')
        self.parent.connectText.grid(row=4, column=0, columnspan=3, padx=50)
        self.parent.spyText.grid(row=5, column=0, columnspan=3, padx=50)
        self.parent.bundaIdBtn.grid(row=6, column=0, columnspan=3, pady=3)
        self.configure(state=tk.DISABLED)
        self.parent.nickInput.configure(state=tk.DISABLED)
        self.parent.pathInput.configure(state=tk.DISABLED)