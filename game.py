import random
import numpy as np

def random_state(row, column):
    board = np.zeros((row, column))
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
        newBoard[x+1][column+2] = "|"
        output += "|\n"
    
    for y in range(column + 2):
        newBoard[row+2][y] = "-"
        output += "-"
    print(output)
    return newBoard
    
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
