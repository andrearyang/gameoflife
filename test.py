from game import random_state
from game import next_board_state
import numpy as np
import matplotlib.pyplot as plt
import time

def show_board(board, pause_time=0.5):
    plt.imshow(board, cmap='Greys', interpolation='nearest')
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.pause(pause_time)
    plt.clf() 

board = random_state(10, 10)
plt.figure()
while True:
    show_board(board)
    board = next_board_state(board)
