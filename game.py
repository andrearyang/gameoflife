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

    for x in range(width):
        newBoard[0][x] += "-"
    
    # if statement for hashtag rendering
        
    # we should prob return matrix rather than string
        
def next_unit_state(initial_state, row, col):
    neighbors = []
    r = len(initial_state)
    c = len(row)

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            
            currRow = row + x;
            currCol = col + y;
            if (0 <= currRow < r and 0 <= currCol < c):
                neighbors.append((initial_state[currRow][currCol]))
    
    for i in range(len(neighbors)):
        if (neighbors(i) == "#"):
            count += 1
    
    if (initial_state[row][col] == "#" and (count == 0 or count == 1)):
        return " "
    elif (initial_state[row][col] == "#" and (count == 2 or count == 3)):
        return "#"
    elif (initial_state[row][col] == "#"):
        return " "
    elif (initial_state[row][col] and count == 3):
        return "#"

def next_board_state(initial_state):
    row = len(initial_state)
    col = len(row)
    newBoard = np.zeroes((row, col))

    for x in range(row):
        for y in range(col):
            new = next_unit_state(initial_state, x, y)
            newBoard[x][y] = new
    
    return newBoard
