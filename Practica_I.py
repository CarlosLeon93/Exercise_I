from tkinter import *

root = Tk()
root.geometry("260x390")

myFrame = Frame(root)
myFrame.grid(column=0, row=0)
myFrame_2 = Frame(root)
myFrame_2.grid(column=0, row=1)


#------------------------Menus------------------------

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
Menu_Ayuda.add_command(label="Licencia")
Menu_Ayuda.add_command(label="Acerca de...")


#-------------------------Text Fields---------------------

textField_1 = Entry(myFrame)
textField_1.grid(column=1, row=0, sticky="e", pady=10, padx=10)
textField_2 = Entry(myFrame)
textField_2.grid(column=1, row=1, sticky="e", pady=10, padx=10)
textField_3 = Entry(myFrame)
textField_3.grid(column=1, row=2, sticky="e", pady=10, padx=10)
textField_4 = Entry(myFrame)
textField_4.grid(column=1, row=3, sticky="e", pady=10, padx=10)
textField_5 = Entry(myFrame)
textField_5.grid(column=1, row=4, sticky="e", pady=10, padx=10)
textField_6 = Text(myFrame, width=15, height=7)
textField_6.grid(column=1, row=5, sticky="e", pady=10, padx=10)


#-------------------------Labels------------------------

Label(myFrame, text="ID:").grid(column=0, row=0, sticky="e", pady=10, padx=10)
Label(myFrame, text="Nombre:").grid(column=0, row=1, sticky="e", pady=10, padx=10)
Label(myFrame, text="Password:").grid(column=0, row=2, sticky="e", pady=10, padx=10)
Label(myFrame, text="Apellido:").grid(column=0, row=3, sticky="e", pady=10, padx=10)
Label(myFrame, text="Dirección:").grid(column=0, row=4, sticky="e", pady=10, padx=10)
Label(myFrame, text="Comentarios:").grid(column=0, row=5, sticky="e", pady=10, padx=10)


#-------------------------Buttons------------------------


Button(myFrame_2, text="Create").grid(column=0,row=0, pady=10, padx=10)
Button(myFrame_2, text="Read").grid(column=1, row=0, pady=10, padx=10)
Button(myFrame_2, text="Update").grid(column=2, row=0, pady=10, padx=10)
Button(myFrame_2, text="Delete").grid(column=3, row=0, pady=10, padx=10)


root.mainloop()