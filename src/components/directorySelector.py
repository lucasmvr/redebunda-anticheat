import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import os

from utils.path import resource_path

class DirectorySelector(tk.Label):
    def __init__(self, root, *args, **kwargs):
        load = Image.open(resource_path('assets/dir.png'))
        load = load.resize((25,25))
        self.render = ImageTk.PhotoImage(load)

        tk.Label.__init__(
            self,
            root,
            image=self.render,
            *args,
            **kwargs
        )

        self.parent = root

        self.bind('<Button-1>', self.click)
    
    def click(self, event):
        if self.cget('state') == tk.DISABLED: return
        path = askdirectory()
        self.parent.pathDescriptor.config(text=path)