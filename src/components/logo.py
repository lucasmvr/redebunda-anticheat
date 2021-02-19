from tkinter import Label
from PIL import Image, ImageTk
import os

from utils.path import resource_path

class Logo(Label):
    def __init__(self, root, *args, **kwargs):
        load = Image.open(resource_path('assets/logo.png'))
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