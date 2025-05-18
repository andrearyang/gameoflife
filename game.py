import random
import numpy as np

def random_state(width, height):
    board = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            board[x][y] = random.randint(0,1)

    return board

def render(board):
    width = len(board)
    length = len(width)
    newBoard = np.zeroes((width, length))

    newBoard[0][0] = "-";
    newBoard[0][1] = "-";

    for x in range(2, width):
        newBoard[0][x] += "-"
    
    # if statement for hashtag rendering
        
    # we should prob return matrix rather than string
        
def next_board_state(board):