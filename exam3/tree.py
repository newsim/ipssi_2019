#!/usr/bin/python3
import sys
from math import floor
def show_tree(width):
    height=floor((width/5))+1
    if (width%2 == 0):
        width=width+1
    if width <= 3:
        tronc=1
    else:
        tronc=3
    tree=""
    for i in range(1,width+1,2):
        tree=tree +(i*"x").center(width)
        tree=tree+"\n"
    for i in range(height):
        if (i<height-1):
            tree=tree+(tronc*"x").center(width)
            tree=tree+"\n"
        else:
            tree=tree+(tronc*"x").center(width)
    return tree


if __name__ == "__main__":
    print(show_tree(int(sys.argv[1])))