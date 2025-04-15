from tkinter import * 
from PIL import Image, ImageTk

root = Tk()
root.title("Tkinter Application with Label and Image")
root.geometry("400x400")  

image_path = "C:\Users\nages\Desktop\Python code files\lesson16\beach.png" 
image = ImageTk.PhotoImage(Image.open(image_path))
l1 = Label(root , image = image )
l1.pack()
l2 = Label(root , text = "This a beach")
l2.pack()
root.mainloop()