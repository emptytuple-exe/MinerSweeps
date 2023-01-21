from tkinter import *
from PIL import Image, ImageTk
import settings
import sys

boomimage = Image.open("images/boom.jpg") #importing 1st image
boom_resized=boomimage.resize((450,300))
flagimage = (Image.open("images/flag.jpg")) #importing 2nd image
flagimage_resized=flagimage.resize((450,300))

def mega():
    global boom_resized
    win=Toplevel()
    win.title("Game over")
    test = ImageTk.PhotoImage(boom_resized)
    flagimage = (Image.open("images/boom.jpg")) #importing 2nd image
    flagimage_resized=flagimage.resize((450,300))
    
    win.geometry(f'{settings.winwidth}x{settings.winheight}')
    win.configure(bg="white")
    #"Game Over" Window

    #def function_for_button1_click():


    #def function_for_button2and3_click():

    frame1=Frame(win,bg="red",width=100,height=500, padx=5, pady=5)
    label1=Label(frame1,image=test,padx=5,pady=5)
    label2=Label(frame1,text="Game Over",bg="white",fg='black',font=("Courier",45))
    button1=Button(frame1,text="Play Again",height=1,width=10,font=("Courier",30),bg="white")
    button2=Button(frame1,text="Exit",height=1,width=10,font=("Courier",30),bg="white", command=sys.exit)
    

    
    label2.grid(column=600,row=300)
    button2.place(x=700,y=225)
    button1.place(x=400,y=225)
    label1.grid(column=1,row=0,padx=10,pady=10, columnspan=2)
    label2.grid(column=1,row=1,padx=10,pady=10,columnspan=2)
    button1.grid(column=1, row=2, padx=10,pady=10)
    button2.grid(column=2, row=2,padx=10,pady=10)
    frame1.place(relx=0.5, rely=0.5,anchor="center")
    win.mainloop()


def mini():
    #"you win" Window
    
    win=Tk()
    win.title("you win")
    test2= ImageTk.PhotoImage(flagimage_resized)
    win.geometry(f'{settings.winwidth}x{settings.winheight}')
    frame2=Frame(win,bg="green",width=100,height=500, padx=5, pady=5)
    label3=Label(frame2,text="You have found all the mines!",bg="white",fg='black',font=("Courier",35))
    label4=Label(frame2,image=test2,padx=5,pady=5)
    button3=Button(frame2,text="Play Again",height=1,width=10,font=("Courier",30),bg="white")
    button4=Button(frame2,text="Exit",height=1,width=10,font=("Courier",30),bg="white",command=sys.exit)
    
  
    label4.grid(column=1,row=0,padx=10,pady=10, columnspan=2)
    label3.grid(column=1,row=1,padx=10,pady=10,columnspan=2)
    button3.grid(column=1, row=2, padx=10,pady=10)
    button4.grid(column=2, row=2,padx=10,pady=10)
    frame2.place(relx=0.5, rely=0.5,anchor="center")
<<<<<<< HEAD
    win.mainloop()
=======
    win.mainloop()
>>>>>>> f531430e4a3d73b528a31888a2ba7de0c05fc28f
