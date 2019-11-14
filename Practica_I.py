from tkinter import *

root = Tk()

myFrame = Frame(root)
myFrame.pack()

Menu_main = Menu(root)
root.config(menu=Menu_main)

Menu_DB = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="DB", menu=Menu_DB)
Menu_DB.add_command(label="Connect")
Menu_DB.add_command(label="Salir")

Menu_Borrar = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="Borrar", menu=Menu_Borrar)
Menu_Borrar.add_command(label="Borrar campos")

Menu_CRUD = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="CRUD", menu=Menu_CRUD)
Menu_CRUD.add_command(label="Create")
Menu_CRUD.add_command(label="Read")
Menu_CRUD.add_command(label="Update")
Menu_CRUD.add_command(label="Delete")

Menu_Ayuda = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="Ayuda", menu=Menu_Ayuda)


root.mainloop()