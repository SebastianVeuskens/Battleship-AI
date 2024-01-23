import numpy as np
import copy 
# import pandas as pd
import utils.exceptions as ue 
import logging   

# TODO: Name the columns by letters -> Transfrom numpy array to pandas 
class Board(): 
    def __init__(self, board_length):
        self.__board_length = board_length 
        self.__board_field = np.zeros((board_length, board_length), dtype=bool)   
        self.__ships = list()  

    def check_rules(self, ship):
        row = ship.row
        col = ship.col
        ship_length = ship.length
        vertical = ship.vertical 

        ########################### 
        #### Verify game rules ####
        ###########################

        # Check basic coordinate compatibility 
        try:
            assert type(col) == int
            assert type(row) == int 
            assert col in range(self.board_length)
            assert row in range(self.board_length)
        except Exception: 
            raise ue.CoordinateException("Ship coordinates are not compatible coordinates within the board!") 

        # Check for border adherence 
        try:
            max_extend = (row + ship_length) * vertical + (col + ship_length) * (1 - vertical) - 1
            assert max_extend < self.board_length
        except Exception:
            raise ue.BorderException("Ship coordinates and length do not confine with the board!")

        # Check for overlapping 
        board_update = np.zeros_like(self.__board_field) 
        if vertical:
            board_update[row:(row + ship_length), col] = 1 
        else:
            board_update[row, col:(col + ship_length)] = 1

        try: 
            assert ~np.any(self.__board_field & board_update)
        except Exception:
            raise ue.OverlapException("Ship overlaps with another ship!")
        
        # Check for boat touching 
        col_lower = max(0, col - 1)
        row_lower = max(0, row - 1)
        if vertical:
            col_upper = min(self.board_length, col + 2)
            row_upper = min(self.board_length, row + ship_length + 1)   
        else:
            col_upper = min(self.board_length, col + ship_length + 1)
            row_upper = min(self.board_length, row + 2) 
            
        update_borders = np.zeros_like(self.__board_field)
        update_borders[row_lower:row_upper, col_lower:col_upper] = 1
        
        try:
            assert ~np.any(self.__board_field & update_borders)
        except Exception:
            raise ue.NeighbourException("Ship touches other ship!")
        
        return board_update
    
    def place_ship(self, ship):
        board_update = self.check_rules(ship) 
        # Place ship 
        self.__board_field = self.__board_field + board_update 
        self.__ships.append(ship)

    def __str__(self): 
        return "Board with ships/n" + str(self.__board_field)
    
    @property
    def board_length(self):
        return np.copy(self.__board_length) 
    
    @property 
    def ships(self):
        return copy.deepcopy(self.__ships)
    
    # TODO: This should not be accessible/give back the field, except for test purposes 
    @property
    def board_field(self):
        print("This is for Test purposes only!")
        return np.copy(self.__board_field) 

    def dimensions(self):
        return self.__board_field.shape 
    
    def game_finished(self, board_status):
        return np.sum(self.__board_field) == np.sum(self.__board_field & board_status)
    
    def hit(self, row, col):
        return self.__board_field[row, col] 