import tkinter as tk
import os

from tkinter import messagebox

class BundaIdButton(tk.Button):
    def __init__(self, root, *args, **kwargs):
        tk.Button.__init__(
            self,
            root,
            text='Bunda ID',
            highlightcolor='#000',
            activeforeground='#AA1',
            pady=5,
            padx=5,
            *args,
            **kwargs
        )
        self.bind('<Button-1>', self.click)
    
    def click(self, event):
        messagebox.showinfo('Bunda ID', 'Seu Bunda ID é:\n'+os.environ['redebunda-anticheat-bundaId'])