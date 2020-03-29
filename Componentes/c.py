from cmenu import *
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.messagebox import showerror, showinfo
import os.path


Root.geometry ("350x150+500+250")
Label(Root, text = "Usuario:").pack()
caja1 = Entry(Root)
caja1.pack()
 
Label(Root, text = "Contraseña:").pack()
caja2 = Entry(Root, show = "*")
caja2.pack()
 
def login():
 # Connect to database
 os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
 db = sqlite3.connect('daily.db')
 c = db.cursor()
  
 usuario = caja1.get()
 contr = caja2.get()
  
 c.execute('SELECT * FROM PASAJEROS WHERE APELNOM= ? AND CLAVE= ?', (usuario, contr))
  
 if c.fetchall():
  showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
 else:
  showerror(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
   
 c.close()
 
Button (text = "Login", command = login).pack()
 






Root.mainloop()