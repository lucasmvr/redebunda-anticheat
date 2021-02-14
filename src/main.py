import tkinter as tk
from PIL import Image, ImageTk

from components.logo import Logo

root = tk.Tk()
root.title('Rede Bunda - Antibatota xD')
root.geometry('400x400')

app = Logo(root)
print(app)
app.pack(side='top')




# load = Image.open('./assets/logo.png')
# load = load.resize((80,80))
# render = ImageTk.PhotoImage(load)

# label = tk.Label(root, image=render)
# label.pack(side='top')

label2 = tk.Label(root, text='Bem vindo ao antibatota da Rede Bunda!\nCuidado, você está sendo monitorado =)')
label2.pack()

# label = tk.Label(root, text='Redebunda =)')
# label.pack(padx=20, pady=20)



root.mainloop()