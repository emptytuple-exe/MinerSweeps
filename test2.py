from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x700")
root.configure(bg="light blue")

image2 = Image.open("mine2.jpg")

resized=image2.resize((400,300),Image.ANTIALIAS)


test = ImageTk.PhotoImage(resized)



label4=Label(root,text="Rules",font=("Times New Roman",35),bg="light green",fg="purple")
label5=Label(root,text="There are a set number of mines present in the given tiles. Select any tile to begin the game",font=("Times New Roman",14),bg="light green",fg="purple")
label6=Label(root,text="The gole of the gamr is to not cick on any mines",font=("Times New Roman",14),bg="light green",fg="purple")
label7=Label(root,text="There are a set number of mines present in the given tiles. Select ant tile to begin teh game",font=("Times New Roman",14),bg="light green",fg="purple")
label8=Label(root,text="The numbers around certain blocks is tell the number of mines present around the block at any given time",font=("Times New Roman",14),bg="light green",fg="purple")
label3=Button(root,text="Click Here To Begin Playing",font=("Times New Roman",20),bg="white",fg="purple")


label1 =Label(image=test)
label1.image = test

# Position image
label1.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
label8.pack()
label3.pack()
root.mainloop()