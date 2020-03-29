from tkinter import *
from tkinter import messagebox
import sqlite3
import os.path
from tkinter.ttk import *




Root= Tk()
BarraMenu= Menu(Root)

Root.config(menu=BarraMenu, width="300", height="300")

bbddMenu=Menu(BarraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar")
bbddMenu.add_separator()
bbddMenu.add_command(label="Salir")

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


