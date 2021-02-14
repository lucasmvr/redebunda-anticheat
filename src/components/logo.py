from tkinter import Label
from PIL import Image, ImageTk


class Logo(Label):
    def __init__(self, master=None):
        load = Image.open('./assets/logo.png')
        load = load.resize((80,80))
        self.render = ImageTk.PhotoImage(load)
        Label.__init__(
            self, 
            master, 
            # bg='#000',
            padx=13,
            pady=13,
            image=self.render
        )