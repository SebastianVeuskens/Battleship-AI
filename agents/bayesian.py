import numpy as np
from default import Agent, convert_index 

# TODO: Implement algorithm that is based on marginal probabilities 

class Bayesian(Agent):
    def __init__(self, *args):
        super().__init__(*args) 
        # self._moves = 
        self.current_index = 0

    def next_move(self):
        # index = self._moves[self.current_index] 
        coordinates = # convert_index(self.length, index)
        self.guess(*coordinates) 
        self.current_index += 1 
        return coordinates 

    