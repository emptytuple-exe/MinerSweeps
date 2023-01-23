from tkinter import *
from PIL import Image, ImageTk
from main import ultra
import settings

def silt():
    hi = Tk()
    hi.title("welcome")
    hi.geometry(f'{settings.winwidth}x{settings.winheight}')
    hi.configure(bg="light blue")

    image1 = Image.open("images/miner.jpg")
    test = ImageTk.PhotoImage(image1)
    label2=Label(hi,text="Minesweeper",font=("Times New Roman",45),bg="light green",fg="purple")

    def test2win():
        hi.destroy()
        hi2 = Tk()
        hi2.title("instructions")
        print(f'{settings.winwidth}x{settings.winheight}')
        hi2.geometry(f'{settings.winwidth}x{settings.winheight}')
        hi2.configure(bg="light blue")

        image2 = Image.open("images/biggerminer.jpg")

        resized=image2.resize((400,300),Image.ANTIALIAS)


        test = ImageTk.PhotoImage(resized)

        frame4=Frame(hi2,bg="light blue",width=100,height=100,padx=5,pady=5)
        label4=Label(frame4,text="Rules",font=("Times New Roman",35),bg="light green",fg="purple")
        label5=Label(frame4,text="There are a set number of mines present in the given tiles. Select any tile to begin the game",font=("Times New Roman",14),bg="light green",fg="purple")
        label6=Label(frame4,text="The goal of the game is to not cick on any mines",font=("Times New Roman",14),bg="light green",fg="purple")
        label7=Label(frame4,text="There are a set number of mines present in the given tiles. Select ant tile to begin teh game",font=("Times New Roman",14),bg="light green",fg="purple")
        label8=Label(frame4,text="The numbers around certain blocks is tell the number of mines present around the block at any given time",font=("Times New Roman",14),bg="light green",fg="purple")

        def mainwin():
            hi2.destroy()
            import main
            ultra()
        label3=Button(frame4,text="Click Here To Begin Playing",font=("Times New Roman",20),bg="white",fg="purple", command=mainwin)

        label1 =Label(frame4,image=test)
        label1.image = test
        frame4.place(relx=0.5,rely=0.5,anchor="center")
        # Position image
        label1.pack()
        label4.pack()
        label5.pack()
        label6.pack()
        label7.pack()
        label8.pack()
        label3.pack()
        hi2.mainloop() 

    frame3=Frame(hi,bg="white",width=100,height=100,padx=5,pady=10)
    label3=Button(frame3,text="Click Here To Play",font=("Times New Roman",20),bg="white",fg="purple", command=test2win)
    label10=Label(frame3,text="Minesweeper",font=("Times New Roman",45),bg="light green",fg="purple")
    label1 =Label(frame3,image=test,padx=5,pady=5)
    label1.image = test
    label10.pack()
    # Position image
    frame3.place(relx=0.5,rely=0.5,anchor="center")
    #frame3.place(relx=5,rely=0.5,anchor="center")
    label1.pack()
    label3.pack()
    #label1.grid(column=1,row=0,padx=10,pady=10,columnspan=2)

    #label1.pack()
    #label3.grid(column=1,row=1,padx=10,pady=10,columnspan=2)
    hi.mainloop()
silt()