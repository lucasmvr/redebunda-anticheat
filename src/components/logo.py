from tkinter import Label
from PIL import Image, ImageTk


class Logo(Label):
    def __init__(self, root, *args, **kwargs):
        load = Image.open('./assets/logo.png')
        load = load.resize((80,80))
        self.render = ImageTk.PhotoImage(load)
        Label.__init__(
            self, 
            root, 
            padx=13,
            pady=13,
            image=self.render,
            *args,
            **kwargs
        )