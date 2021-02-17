import tkinter as tk
import os

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
        
        if not self.parent.codInput.get() or self.parent.codInput.get().split(' ')[0] == '':
            messagebox.showinfo('Calma lá!', 'Você ainda não digitou o código do seu jogo. (:')
            return

        if not self.parent.pathDescriptor.cget('text'):
            messagebox.showinfo('Calma lá!', 'Você precisa selecionar a pasta de instalação do jogo. (:')
            return

        os.environ['redebunda-anticheat-nickname'] = self.parent.nickInput.get()
        os.environ['redebunda-anticheat-codigo'] = self.parent.codInput.get()
        os.environ['redebunda-anticheat-csPath'] = self.parent.pathDescriptor.cget('text')

        try:
            self.parent.socket.start()
            self.parent.socketStarted = True
            self.parent.socket.connectSocket()
        except Exception as e:
            print(e)
            messagebox.showerror('Ops...', 'Ocorreu um erro ao se conectar com o servidor.')
            self.parent.socketStarted = False
            self.parent.connectText.insert(1.0, 'Não foi possível se conectar.')
            self.parent.connectText.tag_add('center', 1.0, 'end')
            return
        
        try:
            self.parent.spy.start(os.environ['redebunda-anticheat-csPath'])
            self.parent.spyStarted = True
        except Exception as e:
            print(e)
            if str(e) == 'ERROR_PATH':
                messagebox.showerror('Ops...', 'Parece que você selecionou a pasta de instalação errada.')
            else:
                messagebox.showerror('Ops...', 'Ocorreu um erro na inicialização do módulo de monitoramento.')
            self.parent.socket.join()
            self.parent.socketStarted = False
            return
        
        try:
            self.parent.screenCapture.start()
            self.parent.screenStarted = True
        except Exception as e:
            print(e)
            messagebox.showerror('Ops...', 'Ocorreu um erro na inicialização do VAR.')
            self.parent.socket.join()
            self.parent.socketStarted = False
            self.parent.spy.stop()
            self.parent.spyStarted = True
            return

        self.parent.connectText.insert(1.0, 'Conectado com o servidor!')
        self.parent.connectText.tag_add('center', 1.0, 'end')
        self.parent.spyText.insert(1.0, 'Você está sendo monitorado xD')
        self.parent.spyText.tag_add('center', 1.0, 'end')
        self.parent.connectText.grid(row=5, column=0, columnspan=3, padx=50)
        self.parent.spyText.grid(row=6, column=0, columnspan=3, padx=50)
        self.parent.bundaIdBtn.grid(row=7, column=0, columnspan=3, pady=3)
        self.configure(state=tk.DISABLED)
        self.parent.nickInput.configure(state=tk.DISABLED)
        self.parent.pathInput.configure(state=tk.DISABLED)
        self.parent.codInput.configure(state=tk.DISABLED)