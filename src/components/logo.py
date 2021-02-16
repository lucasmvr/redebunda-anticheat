from tkinter import Label
from PIL import Image, ImageTk


class Logo(Label):
    def __init__(self, root, *args, **kwargs):
        load = Image.open('./assets/logo.png')
        load = load.resize((50,50))
        self.render = ImageTk.PhotoImage(load)
        Label.__init__(
            self, 
            root, 
            padx=5,
            pady=5,
            image=self.render,
            *args,
            **kwargs
        )