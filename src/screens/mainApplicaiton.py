import tkinter as tk

from components.logo import Logo
from components.textInput import TextInput
from components.loginButton import LoginButton
from components.directorySelector import DirectorySelector
from components.infoText import InfoText
from components.bundaIdButton import BundaIdButton

from screens.header import Header

from static.constants import Constants

from services.socket import Socket
from services.spy import Spy
from services.screenCapture import ScreenCapture

class MainApplicaiton(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(
            self, 
            root,
            )
        self.grid(row=0, column=0)
        ScreenCapture()

        const = Constants(root)
        self.socket = Socket()
        self.socketStarted = False

        self.spy = Spy(self.socket)
        
        self.header = Header(self)
        self.header.grid(row=0, column=0, columnspan=3)

        self.nickLabel = tk.Label(self, text='Nickname: ', font=const.FONT_LABEL)
        self.nickInput = TextInput(self)
        self.nickLabel.grid(row=1, column=0)
        self.nickInput.grid(row=1, column=1, columnspan=2)

        self.codLabel = tk.Label(self, text='Código do jogo: ', font=const.FONT_LABEL)
        self.codInput = TextInput(self)
        self.codLabel.grid(row=2, column=0)
        self.codInput.grid(row=2, column=1, columnspan=2)
    
        self.pathLabel = tk.Label(self, text='Pasta de instalção\ndo C.S. 1.6:', font=const.FONT_LABEL)
        self.pathDescriptor = tk.Label(self, width='15')
        self.pathInput = DirectorySelector(self)
        self.pathLabel.grid(row=3, column=0, pady=5)
        self.pathDescriptor.grid(row=3, column=1, pady=5)
        self.pathInput.grid(row=3, column=2, pady=5)

        self.loginButton = LoginButton(self, font=const.FONT_LABEL)
        self.loginButton.grid(row=4, column=0, columnspan=3, pady=(0, 10))
        
        self.connectText = InfoText(self)

        self.spyText = InfoText(self)
        
        self.bundaIdBtn = BundaIdButton(self, font=const.FONT_LABEL)