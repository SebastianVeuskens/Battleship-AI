import numpy as np
import pandas as pd
import random 
import logging 

class Ship():
    def __init__(self, ship_length = 2, vertical = True, row = None, col = None, board_length = None):
        if not (row and col):
            if not board_length:
                raise Exception("At least one of the two has to be specified: board_length or ship coordinates (row,col)")
            else:
                row = random.randint(0, board_length - 1)
                col = random.randint(0, board_length - 1)
        
        self._row = row 
        self._col = col 
        self._length = ship_length 
        self._vertical = vertical 

    @property 
    def row(self):
        return self._row 
    
    @property 
    def col(self):
        return self._col 
    
    @property 
    def length(self):
        return self._length 
    
    @property 
    def vertical(self):
        return self._vertical 
    

# TODO: Name the columns by letters -> Transfrom numpy array t pandas 
class Board(): 

    def check_rules(self, ship):
        col = ship.col
        row = ship.row
        ship_length = ship.length
        vertical = ship.vertical 

        ########################### 
        #### Verify game rules ####
        ###########################
        # TODO: Create an own Exception class for each error 

        # Check basic coordinate compatibility 
        try:
            assert type(col) == int
            assert type(row) == int 
            assert col in range(self.board_length)
            assert row in range(self.board_length)
        except Exception: 
            raise ValueError("Ship coordinates are not compatible coordinates within the board!") 

        # Check for border adherence 
        try:
            max_extend = (col + ship_length) * vertical + (row + ship_length) * (1 - vertical) - 1
            assert max_extend < self.board_length
        except Exception:
            raise ValueError("Ship coordinates and length do not confine with the board!")

        # Check for overlapping 
        board_update = np.zeros_like(self._board_field) 
        if vertical:
            board_update[row, col:(col + ship_length)] = 1
        else:
            board_update[row:(row + ship_length), col] = 1 

        try: 
            assert ~np.any(self._board_field & board_update)
        except Exception:
            raise ValueError("Ship overlaps with another ship!")
        
        # Check for boat touching 
        col_lower = max(0, col - 1)
        row_lower = max(0, row - 1)
        if vertical:
            col_upper = min(self.board_length, col + ship_length + 1)
            row_upper = min(self.board_length, row + 1) 
        else:
            col_upper = min(self.board_length, col + 1)
            row_upper = min(self.board_length, row + ship_length + 1)   
            
        update_borders = np.zeros_like(self._board_field)
        update_borders[row_lower:row_upper, col_lower:col_upper] = 1
        
        try:
            assert ~np.any(self._board_field & update_borders)
        except Exception:
            raise ValueError("Ship touches other ship!")
        
        return board_update
    
    
    def place_ship(self, ship):
        board_update = self.check_rules(ship) 
        # Place ship 
        self._board_field = self._board_field + board_update 


    def __init__(self, board_length):
        self._board_length = board_length 
        self._board_field = np.zeros((board_length, board_length), dtype=bool)    
        
    def __str__(self): 
        return "Board with ships/n" + str(self._board_field)
    
    @property
    def board_length(self):
        return np.copy(self._board_length) 
    
    # TODO: This should not be accessible/give back the field, except for test purposes 
    @property
    def board_field(self):
        print("This is for Test purposes only!")
        return np.copy(self._board_field) 

    def dimensions(self):
        return self._board_field.shape 
    
    def game_finished(self, board_status):
        return np.sum(self._board_field) == np.sum(self._board_field & board_status)
    
    def hit(self, row, col):
        return self._board_field[row, col] 