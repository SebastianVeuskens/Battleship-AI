import numpy as np
import pandas as pd
import logging 

# TODO: Name the columns by letters -> Transfrom numpy array t pandas 
class Board(): 

    def __init__(self, board_length, ships):
        self._board_length = board_length 
        self._board_field = np.zeros((board_length, board_length), dtype=bool) 
        for ship in ships:
            col = ship["col"]
            row = ship["row"]
            ship_length = ship["length"] 
            vertical = ship["vertical"]

            ########################### 
            #### Verify game rules ####
            ###########################
            # TODO: Create an own Exception class for each error 

            # Check basic coordinate compatibility 
            try:
                assert type(col) == int
                assert type(row) == int 
                assert col in range(board_length)
                assert row in range(board_length)
            except Exception: 
                raise ValueError("Ship coordinates are not compatible coordinates within the board!") 

            # Check for border adherence 
            try:
                max_extend = (col + ship_length) * vertical + (row + ship_length) * (1 - vertical) - 1
                assert max_extend < board_length
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
                col_upper = min(board_length, col + ship_length + 1)
                row_upper = min(board_length, row + 1) 
            else:
                col_upper = min(board_length, col + 1)
                row_upper = min(board_length, row + ship_length + 1)   
                
            update_borders = np.zeros_like(self._board_field)
            update_borders[row_lower:row_upper, col_lower:col_upper] = 1
            
            try:
                assert ~np.any(self._board_field & update_borders)
            except Exception:
                raise ValueError("Ship touches other ship!")
            
            # Place ship 
            self._board_field = self._board_field + board_update 
        
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