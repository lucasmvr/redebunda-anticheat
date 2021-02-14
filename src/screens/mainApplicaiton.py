import tkinter as tk
from components.logo import Logo

class MainApplicaiton(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.logo = Logo(root)
        self.logoLabel = tk.Label(root, text='Bem vindo ao antibatota da Rede Bunda!\nCuidado, você está sendo monitorado =)')
        self.logo.pack(side='top')
        self.logoLabel.pack()
