import tkinter as tk
from tkinter import Menu, ttk
from clsDB import Input
from clsBox import Box 
import os.path
import sqlite3 as lite
from tkinter import *
from  cmenu import *




def submit():
        
        if(nombre.get()!='' and numDni.get()!=""):
            sub_mit = Input(nombre.get(), cmbDNI.get(), numDni.get(),fecNac.get(),tel.get(),email.get(),clave.get(),cmbPais.get())
            sub_mit.setting()
            sub_mit.submit()
        else:
            print("You need to enter a value!")




Root.title("System 1.0")
earn= ttk.Labelframe(Root, text = "Daily ")
earn.grid(column=0, row=0, padx=4, pady=4)
 #nombre
dLabel = ttk.Label(earn, text="Apellido nombre:").grid(column=0, row=0)
nombre = tk.StringVar()
nombreEntry = ttk.Entry(earn, width=13, textvariable=nombre)
nombreEntry.grid(column=1, row=0,padx=10,pady=10)

#myDoc
cmbDNI= tk.StringVar()
dLabel = ttk.Label(earn, text="Tipo DNI:").grid(column=0, row=1)
combo = ttk.Combobox(earn, width=11, height=20, textvariable=cmbDNI)
combo.grid(column=1, row=1, padx=10, pady=10)
b= Box() 
combo['values'] =b.combo_DNI()
#numDni
eLabel = ttk.Label(earn, text="DNI:").grid(column=0, row=2)
numDni = tk.StringVar()
numDniEntry = ttk.Entry(earn, width=13, textvariable=numDni)
numDniEntry.grid(column=1, row=2,padx=10,pady=10)
#fecNac
eLabel = ttk.Label(earn, text="Fecha Nac:").grid(column=0, row=3)
fecNac = tk.StringVar()
fecNacEntry = ttk.Entry(earn, width=13, textvariable=fecNac)
fecNacEntry.grid(column=1, row=3,padx=10,pady=10)

#micountry
cmbPais= tk.StringVar()
dLabel = ttk.Label(earn, text="Pais:").grid(column=2, row=0)
combo = ttk.Combobox(earn, width=11, height=20, textvariable=cmbPais)
combo.grid(column=3, row=0, padx=10, pady=10)
b= Box() 
combo['values'] =b.combo_values_input()
    
#tel
eLabel = ttk.Label(earn, text="Email:").grid(column=2, row=1)
tel = tk.StringVar()
telEntry = ttk.Entry(earn, width=13, textvariable=tel)
telEntry.grid(column=3, row=1,padx=10,pady=10)
#email
eLabel = ttk.Label(earn, text="Tel:").grid(column=2, row=2)
email = tk.StringVar()
emailEntry = ttk.Entry(earn, width=13, textvariable=email)
emailEntry.grid(column=3, row=2,padx=10,pady=10)
#clave
eLabel = ttk.Label(earn, text="Clave:").grid(column=2, row=3)
clave = tk.StringVar()
claveEntry = ttk.Entry(earn, width=13, textvariable=clave)
claveEntry.grid(column=3, row=3,padx=10,pady=10)

# create the action button
action = ttk.Button(earn, text="Agregar", command=submit)
action.grid(column=0, row=4,padx=10,pady=10)

read = ttk.Button(earn, text="Ver", command=submit)
read.grid(column=1, row=4,padx=10,pady=10)


action = ttk.Button(earn, text="Actualizar", command=submit)
action.grid(column=2, row=4)

action = ttk.Button(earn, text="eliminar", command=submit)
action.grid(column=3, row=4)

'''def clearEntry():
        nombre.set("") 
        numDni.set("")
        tel.set("")
        email.set("")
        clave.get("")'''
        
Root.resizable(0,0)
Root.mainloop()