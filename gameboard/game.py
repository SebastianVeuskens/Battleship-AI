import numpy as np 
import time 

from environment import Board, Ship 
from agents import Naive 
import sys
sys.path.append("display") 
from display import Field 

def game(board_length, ship_lengths, Agent="Naive", width=300, height=300, print_move = True, display = True, sleep=None, summary = True): 
    # Create a board to play on
    board = Board(board_length) 
    for ship_length in ship_lengths:
        while True:
            try:
                ship = Ship(ship_length = ship_length, board_length = board_length)
                board.place_ship(ship)
                break 
            except ValueError:
                pass  

    # Create Agents that play the game 
    # TODO: Add a new if statement every for every agent I add
    if Agent == "Naive": 
        agent = Naive(board) 
    else:
        raise Exception("Unknown Agent type")
    
    moves = list() 
    while(~board.game_finished(agent.board_status)):
        cur_move = agent.next_move() 
        moves.append(cur_move) 
    agent.moves = moves 
    
    # Create the visual representation of the field 
    if display:
        field = Field(width, height, board)
        field.run_game(agent.moves, print_move) 

    if summary:
        rounds = len(moves)
        num_cells = np.prod(board.dimensions()) 
        # num_ships = 
        print(f"Game finished after {rounds} rounds!") 
        print(f"Summary statistics: \n -> {rounds * 100 / num_cells}% of all fields were unveiled") 
        # print(f"/n -> {}% of all guesses were a hit.")

    # return (rounds, moves) 