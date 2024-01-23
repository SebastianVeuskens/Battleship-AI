import numpy as np
from agents.default import Agent, convert_index 

# TODO: Implement algorithm that is based on marginal probabilities 

class Bayesian(Agent):
    def __init__(self, *args):
        super().__init__(*args) 
        # self.__moves = 
        self.__current_index = 0

    def longest_ship(self):
        lengths = list()
        for ship in self.__ships:
            lengths.append(ship.length)
        return(max(lengths))

    def probabilities(self):
        ships = self.__ships 
        status = self.__board_status 
        verticales = np.zeros_like(status) 
        horizontals = np.zeros_like(status) 
        # First approach: Don't assume/calculate possible ship positions from already discovered ships 
        # TODO: This information (left ships and discovered ship positions) should be used for better predictions in the future. 
        ### Pseudo-code (for try-and-error)
        # 1. Find all possible ship positions 
        # 2. For each, calculate possible undiscovered ships 
        # 3. Count all ship positions and choose field with highest count 

        cases = np.zeros_like(status) 

    def next_move(self):
        # index = self._moves[self.__current_index] 
        # coordinates = # convert_index(self.length, index)
        self.guess(*coordinates) 
        self.__current_index += 1 
        return coordinates 

    