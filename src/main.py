import tkinter as tk

from screens.mainApplicaiton import MainApplicaiton

root = tk.Tk()
root.title('Rede Bunda - Antibatota xD')
root.geometry('400x450')
root.resizable(False, False) 



main = MainApplicaiton(root)

root.grid_columnconfigure(0, weight=1)
# root.grid_rowconfigure(0, weight=1)

root.mainloop()