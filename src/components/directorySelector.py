import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory

class DirectorySelector(tk.Label):
    def __init__(self, root, *args, **kwargs):
        load = Image.open('./assets/dir.png')
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
        path = askdirectory()
        self.parent.pathDescriptor.config(text=path)