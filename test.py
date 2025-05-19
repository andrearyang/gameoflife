from game import random_state
from game import next_board_state
from game import render
import os
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
# plt.figure()

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(render(board))
    board = next_board_state(board)
    time.sleep(0.2)
