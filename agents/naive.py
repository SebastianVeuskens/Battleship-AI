import numpy as np
from agents.default import Agent, convert_index

class Naive(Agent):
    def __init__(self, *args):
        super().__init__(*args) 
        self.moves = np.arange(self.board_status.size)
        self.moves = np.random.permutation(self.moves)
        self.current_index = 0
    
    def next_move(self):
        index = self.moves[self.current_index] 
        coordinates = convert_index(self.length, index)
        self.guess(*coordinates) 
        self.current_index += 1 
        return coordinates 