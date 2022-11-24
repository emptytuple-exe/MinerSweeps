from tkinter import Button
import random
import settings

class Cell:
    all=list()

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x=x
        self.y=y

        # append object to Cell.all list
        Cell.all.append(self)


    def cr_button_obj(self, loc):
        btn = Button(
            loc,
            #text=f'{self.x}, {self.y}',
            width=6,
            height=2,
        )
        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event, "Left click done in cell.")
        if self.is_mine:
            self.show_mine()
            print("Mine found in cell")
        else:
            self.show_cell()

    def celldata(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y==y:
                return cell

    @property
    def sir_cells(self):
        cells=[
            self.celldata(self.x-1, self.y-1),
            self.celldata(self.x-1, self.y),
            self.celldata(self.x-1, self.y+1),
            self.celldata(self.x, self.y-1),
            self.celldata(self.x+1, self.y-1),
            self.celldata(self.x+1, self.y),
            self.celldata(self.x+1, self.y+1),
            self.celldata(self.x, self.y+1) 
        ]

        cells=[cell for cell in sir_cells if cell is not None]
        return cells

    def show_cell (self):
        print(self.sir_cells)

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
    
    def right_click_actions(self, event):
        print(event)
        print("I am right clicked")
    
    @staticmethod
    def randomise_mines():
        mine_cells=random.sample(
            Cell.all, settings.mine_count
        )
        for cell in mine_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"