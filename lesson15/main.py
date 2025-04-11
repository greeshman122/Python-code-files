from tkinter import *

root = Tk()
root.title(" Sample Window Telling ")
root.geometry("600x600")

l1 = Label(text="Hello User" , fg = "black" , bg = "white")
l1.pack()
b1 = Button(text="Click Me !!" , fg = "balck" , bg = "white")
b1.pack()
e1 = Entry(fg = "yellow" , bg = "blue" , width = 50)
e1.pack()

f1 = Frame(master=root , relief = RAISED , borderwidth = 5)
f1.pack()

l2 = Label(master=f1 , text="SAMPLE FRAME")
l2.pack()

textbox = Text(fg = "green" , bg = "yellow")
textbox.pack()