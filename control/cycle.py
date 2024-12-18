import numpy as np 
import time 
import yaml 
import sys 

# Add project path to enable local module imports 
with open('config.yaml', 'r') as file:
    configs = yaml.safe_load(file)
project_path = configs['project-path']
sys.path.append(project_path)

from gameboard.board import Board 
from gameboard.ship import Ship 
from display.field import Field 
from agents.naive import Naive 
from agents.bayesian import Bayesian 

def solo_game(board_length, ship_lengths, agentName = "Naive", width = 300, height = 300, print_move = True, display = True, sleep=None, summary = True): 
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
    elif agentName == "Bayesian":
        agent = Bayesian(board)
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
        print(f"Summary statistics: \n -> {round(rounds * 100 / num_cells, 2)}% of all fields were unveiled") 
        # print(f"/n -> {}% of all guesses were a hit.")

    # return (rounds, moves) 
        
def main():
    board_length = 7
    # board_length = int(input('Enter length of board: '))
    ship_lengths = (1, 2)
    agentName = "Naive"
    width = 600
    height = 600
    print_move = False
    display = True
    sleep = None
    summary = True
    solo_game(board_length = board_length, 
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