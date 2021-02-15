import tkinter as tk
from PIL import Image, ImageTk

# todo send info to server
def click(event):
    print(event)


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

        self.bind('<Button-1>', click)