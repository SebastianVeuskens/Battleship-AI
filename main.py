import numpy as np 
import time 

from gameboard.board import Board 
from gameboard.ship import Ship 
from agents.agents import Naive 
from display.field import Field 

def game(board_length, ship_lengths, agentName = "Naive", width = 300, height = 300, print_move = True, display = True, sleep=None, summary = True): 
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
    if agentName == "Naive": 
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
        
def main():
    board_length = 10
    # board_length = int(input('Enter length of board: '))
    ship_lengths = (1, 1, 2, 2, 2, 3, 3, 4)
    agentName = "Naive"
    width = 500
    height = 500
    print_move = True
    display = True
    sleep = None
    summary = True
    game(board_length = board_length, 
         ship_lengths = ship_lengths, 
         agentName = agentName,
         width = width,
         height = height,
         print_move = print_move,
         display = display,
         sleep = sleep,
         summary = summary)


if __name__ == '__main__':
    main() 