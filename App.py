import tkinter as tk
from tkinter import Menu, ttk
from clsDB import Input
win = tk.Tk()

BarraMenu= Menu(win)

win.config(menu=BarraMenu, width="300", height="300")

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

win.title("tipoDNI Input")
def submit():
        if(nombre.get()!='' and tipoDNI.get()!=""):
            sub_mit = Input(nombre.get(), tipoDNI.get(), numDni.get(),fecNac.get(),tel.get(),email.get(),clave.get())
            sub_mit.setting()
            sub_mit.submit()
        else:
            print("You need to enter a value!")
    #create label frame for ui
earn= ttk.Labelframe(win, text = "Daily ")
earn.grid(column=0, row=0, padx=4, pady=4)
    # create label for nombre
dLabel = ttk.Label(earn, text="Apellido nombre:").grid(column=0, row=0)
nombre = tk.StringVar()
nombreEntry = ttk.Entry(earn, width=13, textvariable=nombre)
nombreEntry.grid(column=1, row=0,padx=10,pady=10)

eLabel = ttk.Label(earn, text="tipo DNI:").grid(column=0, row=1)
tipoDNI = tk.StringVar()
tipoDNIEntry = ttk.Entry(earn, width=13, textvariable=tipoDNI)
tipoDNIEntry.grid(column=1, row=1,padx=10,pady=10)

eLabel = ttk.Label(earn, text="DNI:").grid(column=0, row=2)
numDni = tk.StringVar()
numDniEntry = ttk.Entry(earn, width=13, textvariable=numDni)
numDniEntry.grid(column=1, row=2,padx=10,pady=10)

eLabel = ttk.Label(earn, text="Fecha Nac:").grid(column=0, row=3)
fecNac = tk.StringVar()
fecNacEntry = ttk.Entry(earn, width=13, textvariable=fecNac)
fecNacEntry.grid(column=1, row=3,padx=10,pady=10)

eLabel = ttk.Label(earn, text="Email:").grid(column=2, row=1)
tel = tk.StringVar()
telEntry = ttk.Entry(earn, width=13, textvariable=tel)
telEntry.grid(column=3, row=1,padx=10,pady=10)

eLabel = ttk.Label(earn, text="Tel:").grid(column=2, row=2)
email = tk.StringVar()
emailEntry = ttk.Entry(earn, width=13, textvariable=email)
emailEntry.grid(column=3, row=2,padx=10,pady=10)

eLabel = ttk.Label(earn, text="Clave:").grid(column=2, row=3)
clave = tk.StringVar()
claveEntry = ttk.Entry(earn, width=13, textvariable=clave)
claveEntry.grid(column=3, row=3,padx=10,pady=10)



    # create the action button
action = ttk.Button(earn, text="submit", command=submit)
action.grid(column=0, row=4)
win.resizable(0,0)
win.mainloop()