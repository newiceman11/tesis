from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.messagebox import showerror, showinfo
import os.path
from testCase import login
class Login():

    
    def login(self):
    # Connect to database
        os.chdir("/home/juampi/Escritorio/Python/Sistema/Programa")
        db = sqlite3.connect('daily.db')
        c = db.cursor()
            
        usuario =caja1.get()
        contr = caja2.get()
            
        c.execute('SELECT * FROM PASAJEROS WHERE APELNOM= ? AND CLAVE= ?', (usuario, contr))
            
        if c.fetchall():
            showinfo(title = "Login correcto", message = "Usuario y contraseña correctos")
        else:
           showinfo(title = "Login incorrecto", message = "Usuario o contraseña incorrecta")
            
        c.close()
    
Root = Tk()
Root.title ("------- Login Python Diario -------")
Root.geometry ("350x150+500+250")
Label(Root, text = "Usuario:").pack()
caja1 = Entry(Root)
caja1.pack()
Label(Root, text = "Contraseña:").pack()
caja2 = Entry(Root, show = "*")
caja2.pack()
Button (text = "Login", command = login).pack()       
    
    
Root.mainloop()