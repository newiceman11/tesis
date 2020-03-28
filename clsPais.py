from tkinter import *
from tkinter import messagebox
import sqlite3
import os.path
from tkinter.ttk import *   
#---------------------FUNCIONES----------
def salir():
    out= messagebox.askquestion("Salir", "¿Desea salir de la aplacación?")
    if out=="yes":
        RootPais.destroy()




def create():

        myConn= sqlite3.Connection("daily.db")
        myCursor= myConn.cursor()
        myCursor.execute("INSERT INTO PAISES VALUES (NULL,'"+miNombre.get()+"')")
        messagebox.showinfo("BBDD","Se ha registrado correctamente")
        myConn.commit()

RootPais= Tk()
BarraMenu= Menu(RootPais)

RootPais.config(menu=BarraMenu, width="300", height="300")

bbddMenu=Menu(BarraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir", command=salir)

borrarMenu=Menu(BarraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(BarraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(BarraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de")

BarraMenu.add_cascade(label="BBDD", menu=bbddMenu)
BarraMenu.add_cascade(label="Borrar", menu=borrarMenu)
BarraMenu.add_cascade(label="Crud", menu=crudMenu)
BarraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


#----------------------COMIENZO DE CAMPOS-------------------
miNombre= StringVar()
myFrame= Frame(RootPais)
myFrame.pack()
txtName=Entry(myFrame, textvariable=miNombre)
txtName.grid(row=0, column=1, padx=10, pady=10)
#---------LABELS-------------------------------------------
nameLabel= Label(myFrame, text="Nombre País: ")
nameLabel.grid(row=0, column=0, padx=10, pady=10)
#-----------------------buttons---------------------------
myFrame2= Frame(RootPais)
myFrame2.pack()
createButton= Button(myFrame2, text="Crear", command=create)
createButton.grid(row=0, column=0, padx=10, pady=10)
RootPais.mainloop()
