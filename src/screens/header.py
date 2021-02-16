import tkinter as tk
from components.logo import Logo

from static.constants import Constants

class Header(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(
            self,
            root,
        )
        self.grid(row=0, column=0, pady=13)

        const = Constants(root)
        
        self.logo = Logo(self)
        self.logoLabel = tk.Label(self, text='Bem vindo ao VAR\n da Rede Bunda!', font=const.FONT_MAIN)

        self.logo.grid(row=0, column=0)
        self.logoLabel.grid(row=1, column=0)