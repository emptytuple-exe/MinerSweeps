game_title="MineSweeper"
winwidth=1600
winheight=800
gsize=6
cellcount=gsize**2
mine_count=(cellcount)//4

def h_pc(perc):
    return(winheight/100)*perc

def w_pc(perc):
    return(winwidth/100)*perc