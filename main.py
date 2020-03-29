import tkinter as tk
from testCase import Win2
 

 
class Win2():
    def __init__(self, root):
        self.root = root
        self.root.geometry("300x300+500+200")
        self.root["bg"] = "navy"
 
def new_window(Win_class):
    global win2
    try:
        if win2.state() == "normal": win2.focus()
    except NameError as e:
        print(e)
        win2 = tk.Toplevel(win)
        Win_class(win2)

win = tk.Tk()
win.geometry("200x200+200+100")
button = tk.Button(win, text="Open new Window")
button['command'] = lambda: new_window(Win2)
button.pack()
text = tk.Text(win, bg='cyan')
text.pack()
win.mainloop()

if __name__=='__main__' or __name__=='__parents_main__':
    test=Win2()