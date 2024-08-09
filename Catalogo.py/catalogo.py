from tkinter import * 
from tkinter.messagebox import *
#import os, sys
from client.gui import Frame, menu_ventana
#import os
def main(): 
    root = Tk()
    root.title("Catalogo de Peliculas")
    #icono = os.path.join(sys.path[0], "./Imagenes/mov.ico")
    #root.iconbitmap(icono)
    root.resizable(0,0)
    root.geometry("1200x550")
    menu_ventana(root)
    root.config(background="#d6fffa")
    app = Frame(root = root) 
    app.mainloop()
    
    root.mainloop()

if __name__ == '__main__':
    main()      





#root.update_idletasks()
#root.update()
#canvas1.itemconfig(blank, state=DISABLED) ...makes blank-button inactive