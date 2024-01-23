import numpy as np
import pandas as pd
import utils.exceptions as ue
import logging 

def convert_index(board_length, index):
    row = index // board_length 
    col = index % board_length 
    return (row, col) 

class Agent():
    def __init__(self, board):
        self.__board = board 
        self.__length = board.board_length
        self.__board_status = np.zeros((self.__length, self.__length), dtype=bool)
        self.__moves = None 
        self.__ships = board.ships 
        
    def guess(self, row, col):
        self.__board_status[row, col] = self.__board.hit(row, col) 

    @property 
    def length(self):
        return self.__length
    
    @property 
    def board_status(self):
        return np.copy(self.__board_status)
    
    @property 
    def moves(self):
        return self.__moves.copy()
    
    @moves.setter
    def moves(self, value):
        self.__moves = value.copy() 

    def next_move(self):
        raise ue.NotImplementedException("The function 'next_move()' is not implemented for this type of class Agent!")