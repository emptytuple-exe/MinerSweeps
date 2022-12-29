from tkinter import *
from PIL import Image, ImageTk
import settings

def mega():

    win=Tk()
    boomimage = Image.open("images/boom.jpg") #importing 1st image
    test = ImageTk.PhotoImage(boomimage)
    flagimage = Image.open("images/flag.jpg") #importing 2nd image
    test2 = ImageTk.PhotoImage(flagimage)
    win.geometry(f'{settings.winwidth}x{settings.winheight}')
    win.configure(bg="white")
    #"Game Over" Window

    #def function_for_button1_click():


    #def function_for_button2and3_click():

    
    label1=Label(image=test)
    label2=Label(win,text="Game Over",bg="white",fg='black',font=("Courier",45))
    button1=Button(win,text="Play Again",height=1,width=10,font=("Courier",30),bg="white")
    button2=Button(win,text="Exit",height=1,width=10,font=("Courier",30),bg="white")


    
    label2.place(x=550,y=150)
    button2.place(x=700,y=225)
    button1.place(x=400,y=225)
    label1.place(x=450, y=0)

    win.mainloop()

def mini():
    #"you win" Window
    win=Tk()
    win.geometry(f'{settings.winwidth}x{settings.winheight}')
    label2=Label(win,text="You have found all the mines!",bg="white",fg='black',font=("Courier",35))
    button1=Button(win,text="Play Again",height=1,width=10,font=("Courier",30),bg="white")
    button2=Button(win,text="Exit",height=1,width=10,font=("Courier",30),bg="white")
    
    label2.place(x=200,y=150)
    button2.place(x=700,y=225)
    button1.place(x=400,y=225)

    win.mainloop()