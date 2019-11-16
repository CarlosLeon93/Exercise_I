from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("260x390")

myFrame = Frame(root)
myFrame.grid(column=0, row=0)
myFrame_2 = Frame(root)
myFrame_2.grid(column=0, row=1)

#--------------------Variables---------------------

variable_Name = StringVar()
variable_Password = StringVar()
variable_LastName = StringVar()
variable_Address = StringVar()
variable_Comments = StringVar()

#--------------------Functions---------------------


def exitApp():
    value = messagebox.askyesno("Exit", "Are you sure?")
    if value == True:
        root.destroy()

def insertData():
    myConnection = sqlite3.connect("../../Programacion/Python/Usuarios")
    myConnection.close()

def deleteTextFields():
    variable_Name.set("")
    variable_Password.set("")
    variable_LastName.set("")
    variable_Address.set("")
    variable_Comments.set("")
    textField_6.delete("1.0", END)


#------------------------Menus------------------------

Menu_main = Menu(root)
root.config(menu=Menu_main)
Menu_DB = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="DB", menu=Menu_DB)
Menu_DB.add_command(label="Connect", command=insertData)
Menu_DB.add_command(label="Salir", command=exitApp)
Menu_Borrar = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="Borrar", menu=Menu_Borrar)
Menu_Borrar.add_command(label="Borrar campos", command=deleteTextFields)
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
textField_1.grid(column=1, row=0, pady=10, padx=10)
textField_2 = Entry(myFrame, textvariable=variable_Name)
textField_2.grid(column=1, row=1, pady=10, padx=10)
textField_3 = Entry(myFrame, textvariable=variable_Password)
textField_3.grid(column=1, row=2, pady=10, padx=10)
textField_3.config(show="*")
textField_4 = Entry(myFrame, textvariable=variable_LastName)
textField_4.grid(column=1, row=3, pady=10, padx=10)
textField_5 = Entry(myFrame, textvariable=variable_Address)
textField_5.grid(column=1, row=4, pady=10, padx=10)
textField_6 = Text(myFrame,width=15, height=7)
textField_6.grid(column=1, row=5, pady=10, padx=10)


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