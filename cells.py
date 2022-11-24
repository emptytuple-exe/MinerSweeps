from tkinter import Button
class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def cr_button_obj(self, loc):
        btn = Button(
            loc,
            text='txt'
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print("I have been left-clicked") 
    
    def right_click_actions(self, event):
        print(event)
        print("I have been right clicked")