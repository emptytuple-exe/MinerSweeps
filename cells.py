from tkinter import Button, Label, messagebox
import random
import settings
import sys

class Cell:
    all=list()
    cell_count_label_object=None
    cell_count=settings.cellcount

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_open = False
        self.x = x
        self.y = y
        self.is_flaggable=False

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
    
    @staticmethod
    def create_cell_count_label(location):
        lbl= Label(
            location,
            text=f'Cells left: {Cell.cell_count}',
            font=('Courier New CYR',),
            bg='blue'
        )
        Cell.cell_count_label_object=lbl

    def left_click_actions(self, event):
        print(event, "Left click done in cell.")
        if self.is_mine:
            self.show_mine()
            import closepage
            print("Mine found in cell")
        else:
            if self.sir_cells_mine == 0:
                for cell_obj in self.sir_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == settings.mine_count:
                messagebox.showwarning("Game Over","Congratulations! You won!")    
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

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

        cells=[cell for cell in cells if cell is not None]
        return cells

    @property
    def sir_cells_mine(self):
        counter=0
        for cell in self.sir_cells:
            if cell.is_mine:
                counter+=1
        return counter

    def show_cell (self):
        if not self.is_open:
            Cell.cell_count-=1
            self.cell_btn_object.configure(text=self.sir_cells_mine)

            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left: {Cell.cell_count}")

            self.cell_btn_object.configure(
                bg='#d9d9d9'
            )

        self.is_open = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        #messagebox.showwarning("Game Over","You clicked on a mine")
        #import closepage


    def right_click_actions(self, event):
        print(event)
        if not self.is_flaggable:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_flaggable = True
        else:
            self.cell_btn_object.configure(
                bg='#d9d9d9'
            )
            self.is_flaggable = False
    
    @staticmethod
    def randomise_mines():
        mine_cells=random.sample(
            Cell.all, settings.mine_count
        )
        for cell in mine_cells:
            cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"