game_title="MineSweeper"
winwidth=1200  #best kept at 1200
winheight=600  #best kept at 600
gsize=6        #best kept at 6
cellcount=gsize**2
mine_count=(cellcount)//4

def h_pc(perc):
    return(winheight/100)*perc

def w_pc(perc):
    return(winwidth/100)*perc