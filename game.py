import random
import numpy as np

def random_state(row, column):
    board = np.zeros((row, column), dtype=int)
    for x in range(row):
        for y in range(column):
            board[x][y] = random.randint(0,1)

    return board

def render(board):
    row = len(board)
    column = len(board[0])
    newBoard = np.empty((row + 2, column + 2), dtype=str)
    output = ""

    for y in range(column + 2):
        newBoard[0][y] = "-"
        output += "-"
    output += "\n"

    for x in range(row):
        newBoard[x+1][0] = "|"
        output += "|"
        for y in range(column):
            if board[x][y] == 1:
                newBoard[x+1][y+1] = "#"
                output += "#"
            else:
                newBoard[x+1][y+1] += " "
                output += " "
        newBoard[x+1][column+1] = "|"
        output += "|\n"
    
    for y in range(column + 2):
        newBoard[row+1][y] = "-"
        output += "-"
    return output        
        
def next_unit_state(initial_state, row, col):
    neighbors = 0
    r = len(initial_state)
    c = len(initial_state[0])

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            
            currRow = row + x
            currCol = col + y
            if (0 <= currRow < r and 0 <= currCol < c):
                if initial_state[currRow][currCol] == 1:
                    neighbors += 1
    
    if initial_state[row][col] == 1:
        if neighbors < 2 or neighbors > 3:
            return 0
        else:
            return 1
    else:
        if neighbors == 3:
            return 1
        else:
            return 0

def next_board_state(initial_state):
    row = len(initial_state)
    col = len(initial_state[0])
    newBoard = np.zeros((row, col), dtype=int)

    for x in range(row):
        for y in range(col):
            newBoard[x][y] = next_unit_state(initial_state, x, y)
    
    return newBoard

def load_board_state(path):
    try:
        output = np.genfromtxt(path, delimiter = " ", dtype=int)
    except FileNotFoundError:
        return "file not found"
    return output
