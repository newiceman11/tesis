'''from tkinter import *

class First(Frame):
    def __init__(self,master):
        super().__init__()
        master.minsize(width=755, height=520)
        master.maxsize(width=755, height=520)
        Grid.config(self)

        # Run all function in [First Class]
        self.widget_size()


    def widget_size(self):

        # Define a small frame for it
        self.main_inner_frame = LabelFrame(self,text="Tracing Method",height= 120,width =355)
        self.main_inner_frame.grid(row= 0, column=0)
        self.main_inner_frame.grid_propagate(0)

        # Create a entry box for the user
        # use a string variable tvar
        tvar = StringVar()
        self.traceEntry = Entry(self.main_inner_frame,textvariable=tvar,width=30)
        self.traceEntry.grid(row = 0, column = 2, sticky = W)

        # Create a button for it [When trace click it will show the text in the entry on terminal]
        self.traceButton = Button(self.main_inner_frame, text="Trace",command=lambda: Second.printSecondLine(tvar))
        self.traceButton.grid(row = 0, column = 1, sticky = W)


class Second(First):
    @staticmethod
    def __init__(self,master):
        super().__init__(master)

    @staticmethod
    def printSecondLine(value):
        print(value.get())


if __name__ == '__main__':
    root = Tk()
    root.title("Good System")
    TIF = First(root)
    root.mainloop()'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
# www.pythondiario.com
 
from tkinter import *
from tkinter import messagebox
import sqlite3
from tkinter.messagebox import showerror, showinfo
import os.path


Root = Tk()
Root.title ("------- Login Python Diario -------")
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