import random
import numpy as num

def random_state(width, height):
    board = num.zeroes((width, height))
    for x in width:
        for y in height:
            board[x][y] = random.randInt(0,1)

    return board;
