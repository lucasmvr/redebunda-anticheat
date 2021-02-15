import tkinter as tk


class InfoText(tk.Text):
    def __init__(self, root, *args, **kwargs):
        tk.Text.__init__(
            self,
            root,
            height=1,
            highlightthickness=0,
            width=42,
            *args,
            **kwargs,
        )
        self.tag_configure('center', justify='center')