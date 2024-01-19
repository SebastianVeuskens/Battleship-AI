import random 
import utils.exceptions as ue

class Ship():
    def __init__(self, ship_length = 2, vertical = True, row = None, col = None, board_length = None):
        if (row is None) or (col is None):
            if not board_length:
                raise ue.CoordinateException("At least one of the two has to be specified: board_length or ship coordinates (row,col)")
            else:
                row = random.randint(0, board_length - (ship_length * vertical) - 1)
                col = random.randint(0, board_length - (ship_length * (not vertical)) - 1)
        
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