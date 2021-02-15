import tkinter as tk

class TextInput(tk.Entry):
    def __init__(self, root, *args, **kwargs):
        tk.Entry.__init__(
            self,
            root,
            *args,
            **kwargs
        )