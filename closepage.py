from tkinter import *
from PIL import Image, ImageTk
import settings


boomimage = Image.open("images/boom.jpg") #importing 1st image
boom_resized=boomimage.resize((450,300))
   
def mega():
    global boom_resized
    win=Toplevel()
    test = ImageTk.PhotoImage(boom_resized)
    flagimage = (Image.open("images/boom.jpg")) #importing 2nd image
    test2 = ImageTk.PhotoImage(flagimage)
    win.geometry(f'{settings.winwidth}x{settings.winheight}')
    win.configure(bg="white")
    #"Game Over" Window

    #def function_for_button1_click():


    #def function_for_button2and3_click():

    frame1=Frame(win,bg="red",width=100,height=500, padx=5, pady=5)
    label1=Label(frame1,image=test,padx=5,pady=5)
    label2=Label(win,text="Game Over",bg="white",fg='black',font=("Courier",45))
    button1=Button(frame1,text="Play Again",height=1,width=10,font=("Courier",30),bg="white")
    button2=Button(frame1,text="Exit",height=1,width=10,font=("Courier",30),bg="white")
    

    
    #label2.grid(column=600,row=300)
    #button2.place(x=700,y=225)
    #button1.place(x=400,y=225)
    label1.grid(column=1,row=0,padx=10,pady=10, columnspan=2)
    button1.grid(column=1, row=1, padx=10,pady=10)
    button2.grid(column=2, row=1,padx=10,pady=10)
    frame1.place(relx=0.5, rely=0.5,anchor="center")


    win.mainloop()
mega()


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