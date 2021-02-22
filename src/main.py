import tkinter as tk

from screens.mainApplication import MainApplication

from utils.path import resource_path

import multiprocessing

def main():
    root = tk.Tk()
    root.title('Rede Bunda - VAR xD')
    root.geometry('450x500')
    root.resizable(False, False)
    photo = tk.PhotoImage(file=resource_path('assets/logo.png'))
    root.iconphoto(False, photo)

    main = MainApplication(root)


    def on_closing():
        if main.socketStarted:
            print('socket stop')
            main.socket.disconnect()
            print('socket stop')
        # if main.screenStarted:
        #     main.screenCapture.terminate()
        #     print('screenCapture stop')
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)

    root.grid_columnconfigure(0, weight=1)
    # root.grid_rowconfigure(0, weight=1)

    root.mainloop()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()