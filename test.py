from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x700")
root.configure(bg="light blue")

image1 = Image.open("mine.jpg")
test = ImageTk.PhotoImage(image1)
label2=Label(root,text="Minesweeper",font=("Times New Roman",45),bg="light green",fg="purple")
label3=Button(root,text="Click Here To Play",font=("Times New Roman",20),bg="white",fg="purple")


label1 =Label(image=test)
label1.image = test
label2.pack()
# Position image
label1.pack()
label3.pack()
root.mainloop()