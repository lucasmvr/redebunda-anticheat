import tkinter as tk
from PIL import Image, ImageTk

from screens.mainApplicaiton import MainApplicaiton

root = tk.Tk()
root.title('Rede Bunda - Antibatota xD')
root.geometry('400x400')

main = MainApplicaiton(root)


root.mainloop()