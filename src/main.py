import tkinter as tk
from tkinter import messagebox

from screens.mainApplicaiton import MainApplicaiton

import threading

root = tk.Tk()
root.title('Rede Bunda - Antibatota xD')
root.geometry('400x450')
root.resizable(False, False)
photo = tk.PhotoImage(file='./assets/logo.png')
root.iconphoto(False, photo)


main = MainApplicaiton(root)

def on_closing():
    if main.socketStarted:
        main.socket.join()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

root.mainloop()