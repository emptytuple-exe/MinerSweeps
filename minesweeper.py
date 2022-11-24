from tkinter import *
import settings
from cells import Cell

root = Tk()
root.configure(bg="black") #sets colour of background
root.geometry(f'{settings.winwidth}x{settings.winheight}') #sets size of background
root.title('Mine') #sets title of GUI window
root.resizable(False, False) #controls whether (width, height) of window can be altered

top_frame = Frame(
    root,
    bg='red',
    width=settings.winwidth,
    height=settings.h_pc(25)
)

left_frame = Frame(
    root,
    bg='blue',
    width=settings.w_pc(25),
    height=settings.h_pc(75)
)

centre_frame = Frame(
    root,
    bg='blue',
    width=settings.w_pc(75),
    height=settings.h_pc(75)
)

top_frame.place(x=0, y=0)
left_frame.place(x=0, y=settings.h_pc(25))
centre_frame.place(x=settings.w_pc(25), y=settings.h_pc(25))

'''
btn1= Button(
    centre_frame,
    bg='blue',
    text='lol'
)
btn1.place(x=0, y=0)
'''

'''
c1=Cell()
c1.cr_button_obj(centre_frame)
c1.cell_btn_object.place(
    x=0, y=0
)
'''

'''
c1=Cell()
c1.cr_button_obj(centre_frame)
c1.cell_btn_object.grid(
    column=0, row=0
)
'''

for i in range(settings.gsize):
    for j in range(settings.gsize):
        c=Cell()
        c.cr_button_obj(centre_frame)
        c.cell_btn_object.grid(
            column=i, row=j
        )   

root.mainloop() #runs window