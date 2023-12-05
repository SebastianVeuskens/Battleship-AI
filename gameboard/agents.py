import numpy as np
import pandas as pd
import logging 

def convert_index(board_length, index):
    row = index // board_length 
    col = index % board_length 
    return (row, col) 

class Agent():
    def __init__(self, board):
        self.board = board 
        self.length = board.board_length
        self._board_status = np.zeros((self.length, self.length), dtype=bool)
        
    def guess(self, row, col):
        self._board_status[row, col] = self.board.hit(row, col) 

    @property 
    def board_status(self):
        return np.copy(self._board_status)

    def next_move(self):
        raise Exception("The function 'next_move()' is not implemented for this type of class Agent!")

class Naive(Agent):
    def __init__(self, *args):
        super().__init__(*args) 
        self.moves = np.arange(self.board_status.size)
        np.random.shuffle(self.moves)
        self.current_index = 0
    
    def next_move(self):
        index =  self.moves[self.current_index] 
        coordinates = convert_index(self.length, index)
        self.guess(*coordinates) 
        self.current_index += 1 
        return coordinates 