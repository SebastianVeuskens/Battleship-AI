import numpy as np 
import time 

from environment import Board 
from agents import Naive 
import sys
sys.path.append("display") 
from display import Field 

def game(board_length, ships, Agent="Naive", width=300, height=300, sleep=None): 
    # Create a board to play on
    board = Board(board_length, ships) 

    # Create Agents that play the game 
    if Agent == "Naive": 
        agent = Naive(board) 
    else:
        raise Exception("Unknown Agent type")
    
    # Create the visual representation of the field 
    # field = Field(width, height, board)
    
    moves = list() 
    while ~board.game_finished(agent.board_status): 
        move = agent.next_move() 
        # field.update(move)
        moves.append(move)
        if sleep:
            time.sleep(sleep)

    rounds = len(moves)
    num_cells = np.prod(board.dimensions()) 
    # num_ships = 
    print(f"Game finished after {rounds} rounds!") 
    print(f"Summary statistics: \n -> {rounds / num_cells}% of all fields were unveiled") 
    # print(f"/n -> {}% of all guesses were a hit.")

    return (rounds, moves) 