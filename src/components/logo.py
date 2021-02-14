from tkinter import Label
from PIL import Image, ImageTk


class Logo(Label):
    def __init__(self, master=None):
        load = Image.open('./assets/logo.png')
        load = load.resize((80,80))
        render = ImageTk.PhotoImage(load)
        Label.__init__(
            self, 
            master, 
            bg='#000',
            padx=10,
            pady=10,
            image=render
        )