from tkinter import *
from PIL import Image, ImageTk
#from main import ultra

hi = Tk()
hi.geometry("500x700")
hi.configure(bg="light blue")

image1 = Image.open("mine.jpg")
test = ImageTk.PhotoImage(image1)
label2=Label(hi,text="Minesweeper",font=("Times New Roman",45),bg="light green",fg="purple")


def test2win():
    hi.destroy()
    hi2 = Tk()
    hi2.geometry("800x700")
    hi2.configure(bg="light blue")

    image2 = Image.open("mine2.jpg")

    resized=image2.resize((400,300),Image.ANTIALIAS)


    test = ImageTk.PhotoImage(resized)



    label4=Label(hi2,text="Rules",font=("Times New Roman",35),bg="light green",fg="purple")
    label5=Label(hi2,text="There are a set number of mines present in the given tiles. Select any tile to begin the game",font=("Times New Roman",14),bg="light green",fg="purple")
    label6=Label(hi2,text="The gole of the gamr is to not cick on any mines",font=("Times New Roman",14),bg="light green",fg="purple")
    label7=Label(hi2,text="There are a set number of mines present in the given tiles. Select ant tile to begin teh game",font=("Times New Roman",14),bg="light green",fg="purple")
    label8=Label(hi2,text="The numbers around certain blocks is tell the number of mines present around the block at any given time",font=("Times New Roman",14),bg="light green",fg="purple")


    def mainwin():
        hi2.destroy()
        import main
    label3=Button(hi2,text="Click Here To Begin Playing",font=("Times New Roman",20),bg="white",fg="purple", command=mainwin)


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
    hi2.mainloop() 

label3=Button(hi,text="Click Here To Play",font=("Times New Roman",20),bg="white",fg="purple", command=test2win)

label1 =Label(image=test)
label1.image = test
label2.pack()
# Position image
label1.pack()
label3.pack()
hi.mainloop()