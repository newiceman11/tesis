import tkinter as tk
from tkinter import ttk
from clsDB import Input

win = tk.Tk()
win.title("Earning Input")
def submit():
        if(nombre.get()!='' and tipoDNI.get()!=""):
            sub_mit = Input(nombre.get(), tipoDNI.get())
            sub_mit.setting()
            sub_mit.submit()
        else:
            print("You need to enter a value!")
    #create label frame for ui
earn= ttk.Labelframe(win, text = "Daily Earning Input")
earn.grid(column=0, row=0, padx=4, pady=4)
    # create label for description
dLabel = ttk.Label(earn, text="Nombre:").grid(column=0, row=0)
nombre = tk.StringVar()
nombreEntry = ttk.Entry(earn, width=13, textvariable=nombre)
nombreEntry.grid(column=1, row=0, padx=10, pady=10)

eLabel = ttk.Label(earn, text=" Tipo DNI:").grid(column=0, row=1)
tipoDNI = tk.StringVar()
tipoDNIEntry = ttk.Entry(earn, width=13, textvariable=tipoDNI)
tipoDNIEntry.grid(column=1, row=1, padx=10, pady=10)


eLabel = ttk.Label(earn, text="Número DNI:").grid(column=0, row=2)
tipoDNI = tk.StringVar()
tipoDNIEntry = ttk.Entry(earn, width=13, textvariable=tipoDNI)
tipoDNIEntry.grid(column=1, row=2, padx=10, pady=10)

eLabel = ttk.Label(earn, text="Fecha Nac:").grid(column=0, row=3)
fecNac = tk.StringVar()
fecNac = ttk.Entry(earn, width=13, textvariable=fecNac)
fecNac.grid(column=1, row=3, padx=10, pady=10)

#----------CMB--------------------------------------







#----------CMB--------------------------------------


eLabel = ttk.Label(earn, text="Email:").grid(column=2, row=1)
email = tk.StringVar()
email = ttk.Entry(earn, width=13, textvariable=email)
email.grid(column=3, row=1, padx=10, pady=10)

eLabel = ttk.Label(earn, text="Tel:").grid(column=2, row=2)
tel = tk.StringVar()
tel = ttk.Entry(earn, width=13, textvariable=tel)
tel.grid(column=3, row=2, padx=10, pady=10)

eLabel = ttk.Label(earn, text="Clave:").grid(column=2, row=3)
clave = tk.StringVar()
clave = ttk.Entry(earn, width=13, textvariable=clave)
clave.grid(column=3, row=3, padx=10, pady=10)








# create the action button
action = ttk.Button(earn, text="submit", command=submit)
action.grid(column=0, row=5)
win.resizable(0,0)
win.mainloop()