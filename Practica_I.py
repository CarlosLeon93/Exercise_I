#|-------------------|
#|-->First Project<--|
#|-------------------|
from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("DB Creator 1.0")

myFrame = Frame(root)
myFrame.grid(column=0, row=0)
myFrame_2 = Frame(root)
myFrame_2.grid(column=0, row=1)


#--------------------Variables---------------------


variable_Name = StringVar()
variable_Password = StringVar()
variable_LastName = StringVar()
variable_Address = StringVar()


#--------------------Functions---------------------


def exitApp():
    value = messagebox.askyesno("Exit", "Are you sure?")
    if value == True:
        root.destroy()

def newDB():
    myConnection = sqlite3.connect("../../Programacion/Python/Usuarios")
    myCursor = myConnection.cursor()

    myCursor.execute('''CREATE TABLE USUARIOS(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE VARCHAR(50),
        PASSWORD_ VARCHAR(50),
        APELLIDOS VARCHAR(50),
        ADDRESS_ VARCHAR(50),
        COMMENT VARCHAR(100)
    )''') 

    myConnection.commit()
    myConnection.close()
    messagebox.showinfo("Done", "New DataBase has been created successfully")

def deleteTextFields():

    variable_Name.set("")
    variable_Password.set("")
    variable_LastName.set("")
    variable_Address.set("")
    commentField.delete("1.0", END)

def createDB():
    myConnection = sqlite3.connect("../../Programacion/Python/Usuarios")
    myCursor = myConnection.cursor()
    values = (
        textField_2.get(),
        textField_3.get(),
        textField_4.get(),
        textField_5.get(),
        commentField.get("1.0", END)
    )
    myCursor.execute("INSERT INTO USUARIOS VALUES (NULL,?,?,?,?,?)", values)
    myConnection.commit()
    myConnection.close()
    messagebox.showinfo("Done","New register has been created successfully")
    variable_Name.set("")
    variable_Password.set("")
    variable_LastName.set("")
    variable_Address.set("")
    commentField.delete("1.0", END) 

def readDB():
    try:
        myConnection = sqlite3.connect("../../Programacion/Python/Usuarios")
        myCursor = myConnection.cursor()
        myCursor.execute("SELECT * FROM USUARIOS WHERE ID=?", textField_1.get())
        values = myCursor.fetchall()
        for user in values:
            variable_Name.set(user[1])
            variable_Password.set(user[2])
            variable_LastName.set(user[3])
            variable_Address.set(user[4])
            commentField.delete("1.0", END)
            commentField.insert(END,user[5])
        myConnection.commit()
        myConnection.close()
    except sqlite3.ProgrammingError:
        messagebox.showwarning("Warning","No \"ID\" element added")

def updateDB():
    if textField_1.get() != "":
        myConnection = sqlite3.connect("../../Programacion/Python/Usuarios")
        myCursor = myConnection.cursor()
        values = (
            textField_2.get(),
            textField_3.get(),
            textField_4.get(),
            textField_5.get(),
            commentField.get("1.0", END),
            textField_1.get()
        )
        myCursor.execute("UPDATE USUARIOS SET NOMBRE=?, PASSWORD_=?, APELLIDOS=?, ADDRESS_=?, COMMENT=? WHERE ID=?", values)
        myConnection.commit()
        myConnection.close()
        messagebox.showinfo("Done", "Register has been updated successfully")
    else:
        messagebox.showwarning("Warning","No \"ID\" element added")

def deleteDB():
    try:
        value=messagebox.askyesno("Delete Resgister", "Are you sure?")
        if value == True:
            myConnection = sqlite3.connect("../../Programacion/Python/Usuarios")
            myCursor = myConnection.cursor()
            myCursor.execute("DELETE FROM USUARIOS WHERE ID=?", textField_1.get())
            myConnection.commit()
            myConnection.close()
            messagebox.showinfo("Done", "Register deleted successfully")
        else:
            messagebox.showwarning("Cancelled", "Register has not been deleted")
    except sqlite3.ProgrammingError:
        messagebox.showwarning("Warning","No \"ID\" element added")


#------------------------Menus------------------------


Menu_main = Menu(root)
root.config(menu=Menu_main)
Menu_DB = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="DB", menu=Menu_DB)
Menu_DB.add_command(label="Connect", command=newDB)
Menu_DB.add_command(label="Salir", command=exitApp)
Menu_Borrar = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="Borrar", menu=Menu_Borrar)
Menu_Borrar.add_command(label="Borrar campos", command=deleteTextFields)
Menu_CRUD = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="CRUD", menu=Menu_CRUD)
Menu_CRUD.add_command(label="Create", command=createDB)
Menu_CRUD.add_command(label="Read", command=readDB)
Menu_CRUD.add_command(label="Update", command=updateDB)
Menu_CRUD.add_command(label="Delete", command=deleteDB)
Menu_Ayuda = Menu(Menu_main, tearoff=0)
Menu_main.add_cascade(label="Ayuda", menu=Menu_Ayuda)
Menu_Ayuda.add_command(label="Licencia")
Menu_Ayuda.add_command(label="Acerca de...")


#-------------------------Text Fields---------------------


textField_1 = Entry(myFrame)
textField_1.grid(column=1, row=0, pady=10, padx=10)
textField_2 = Entry(myFrame, textvariable=variable_Name)
textField_2.grid(column=1, row=1, pady=10, padx=10)
textField_2.config(fg="red", justify="right")
textField_3 = Entry(myFrame, textvariable=variable_Password)
textField_3.grid(column=1, row=2, pady=10, padx=10)
textField_3.config(show="*")
textField_4 = Entry(myFrame, textvariable=variable_LastName)
textField_4.grid(column=1, row=3, pady=10, padx=10)
textField_5 = Entry(myFrame, textvariable=variable_Address)
textField_5.grid(column=1, row=4, pady=10, padx=10)
commentField = Text(myFrame, width=15, height=7)
commentField.grid(column=1, row=5, pady=10, padx=10)


#----------------------------Bar--------------------------


bar=Scrollbar(myFrame, command=commentField.yview)
bar.grid(row=5, column=2, sticky="nsew", pady=10)
commentField.config(yscrollcommand=bar.set)


#-------------------------Labels------------------------


Label(myFrame, text="ID:").grid(column=0, row=0, sticky="e", pady=10, padx=10)
Label(myFrame, text="Nombre:").grid(column=0, row=1, sticky="e", pady=10, padx=10)
Label(myFrame, text="Password:").grid(column=0, row=2, sticky="e", pady=10, padx=10)
Label(myFrame, text="Apellido:").grid(column=0, row=3, sticky="e", pady=10, padx=10)
Label(myFrame, text="Dirección:").grid(column=0, row=4, sticky="e", pady=10, padx=10)
Label(myFrame, text="Comentarios:").grid(column=0, row=5, sticky="e", pady=10, padx=10)


#-------------------------Buttons------------------------


Button(myFrame_2, text="Create",command=createDB).grid(column=0,row=0, pady=10, padx=10)
Button(myFrame_2, text="Read", command=readDB).grid(column=1, row=0, pady=10, padx=10)
Button(myFrame_2, text="Update", command=updateDB).grid(column=2, row=0, pady=10, padx=10)
Button(myFrame_2, text="Delete", command=deleteDB).grid(column=3, row=0, pady=10, padx=10)


root.mainloop()