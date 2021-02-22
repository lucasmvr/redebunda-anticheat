import tkinter as tk
import os

from tkinter import messagebox

class LoginButton(tk.Button):
    def __init__(self, root, *args, **kwargs):
        tk.Button.__init__(
            self,
            root,
            text='Entrar',
            pady=5,
            padx=5,
            *args,
            **kwargs
        )
        self.parent = root
        self.bind('<Button-1>', self.click)
    
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
            self.parent.socket.connectSocket()
            self.parent.socketStarted = True
        except Exception as e:
            print(e)
            if self.parent.socketStarted:
                self.parent.socket.disconnect()
            messagebox.showerror('Ops...', 'Ocorreu um erro ao se conectar com o servidor.')
            self.parent.socketStarted = False
            self.parent.connectText.insert(1.0, 'Não foi possível se conectar.')
            self.parent.connectText.tag_add('center', 1.0, 'end')
            return
        
        try:
            self.parent.spy.start()
            self.parent.spyStarted = True
        except Exception as e:
            print(e)
            if str(e) == 'ERROR_PATH':
                messagebox.showerror('Ops...', 'Parece que você selecionou a pasta de instalação errada.')
            else:
                messagebox.showerror('Ops...', 'Ocorreu um erro na inicialização do módulo de monitoramento.')
            self.parent.socket.disconnect()
            self.parent.socketStarted = False
            return
        
        # try:
        #     self.parent.screenCapture.start()
        #     self.parent.screenStarted = True
        # except Exception as e:
        #     print(e)
        #     messagebox.showerror('Ops...', 'Ocorreu um erro na inicialização do VAR.')
        #     self.parent.socket.disconnect()
        #     self.parent.socketStarted = False
        #     self.parent.spy.stop()
        #     self.parent.spyStarted = True
        #     return
        
        self.logged_app()

    def logged_app(self):
        self.parent.nickLabel.grid_remove()
        self.parent.nickInput.grid_remove()
        self.parent.codLabel.grid_remove()
        self.parent.codInput.grid_remove()
        self.parent.pathLabel.grid_remove()
        self.parent.pathDescriptor.grid_remove()
        self.parent.pathInput.grid_remove()
        self.parent.loginButton.grid_remove()

        self.parent.header.logoLabel.configure(text='Bem vindo ao VAR\n da Rede Bunda, {}!'.format(os.environ['redebunda-anticheat-nickname']))
        self.parent.loggedText.insert(
            1.0,
            'Você está conectado com o servidor!\n\nSeu jogo é {}\n\nSua pasta de instalação do C.S. 1.6 é \n{}\n\nVocê está sendo monitorado xD'.format(
                os.environ['redebunda-anticheat-codigo'],
                os.environ['redebunda-anticheat-csPath']
            ))
        self.parent.loggedText.tag_add('center', 1.0, 'end')
        self.parent.loggedText.grid(row=1, column=0, columnspan=3, padx=50, pady=7)
        self.parent.bundaIdBtn.grid(row=7, column=0, columnspan=3, pady=3)