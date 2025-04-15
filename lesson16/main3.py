from tkinter import *

root = Tk()
root.geometry("4000x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2 = Label(top , text = "This is toplevel window")
    l2.pack()
    top.mainloop()
l = Label(root , text = "This is a root window")
btn = Button(root , text = "Click here to open anoter window" , command = topwin)

l.pack()
btn.pack()