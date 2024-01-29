import numpy as np 
import time 

# import sys 
# sys.path.append('G:/My Drive/Sonstiges/Projects/Battleship-AI')
from gameboard.board import Board 
from gameboard.ship import Ship 
from display.field import Field 
from agents.naive import Naive 
from agents.bayesian import Bayesian 
import utils.exceptions as ue

def random_ships(board, ship_lengths):
    for ship_length in ship_lengths:
        while True:
            try:
                ship = Ship(ship_length = ship_length, board_length = board.board_length)
                board.place_ship(ship)
                break 
            # TODO: Check what ValueError does here exactly, maybe replace it? 
            except ue.RulesException:
                pass  

def get_agent(board, agent_name):
    # TODO: Add a new if statement every for every agent I add
    if agent_name == 'Naive': 
        agent = Naive(board) 
    elif agent_name == 'Bayesian':
        agent = Bayesian(board)
    else:
        raise Exception('Unknown Agent type')
    return agent

def summarize(moves, board):
        rounds = len(moves)
        dims = board.dimensions()
        num_cells = np.prod(dims) 
        num_ships = len(board.ships)
        print(f'There were {num_ships} ships on a {dims[0]}x{dims[1]} board!')
        print(f'Game finished after {rounds} rounds!') 
        print(f'Summary statistics: \n -> {round(rounds * 100 / num_cells, 2)}% of all fields were unveiled') 
        # print(f'/n -> {}% of all guesses were a hit.')

def solo_game(board_length, ship_lengths, agent_name = 'Naive', width = 300, height = 300, print_move = True, display = True, sleep=None, summary = True): 
    # Create a board to play on
    board = Board(board_length) 
    # Place random ships on that board 
    random_ships(board, ship_lengths)

    agent = get_agent(board, agent_name)
    
    moves = list() 
    while(~board.game_finished(agent.board_status)):
        cur_move = agent.next_move() 
        moves.append(cur_move) 
    agent.moves = moves 
    
    # Create the visual representation of the field 
    if display:
        field = Field(width, height, board)
        field.field_ai()
        field.buttons() 
        field.run_game(agent.moves, print_move) 

    if summary: summarize(moves, board)
        # rounds = len(moves)
        # num_cells = np.prod(board.dimensions()) 
        # # num_ships = 
        # print(f'Game finished after {rounds} rounds!') 
        # print(f'Summary statistics: \n -> {round(rounds * 100 / num_cells, 2)}% of all fields were unveiled') 
        # # print(f'/n -> {}% of all guesses were a hit.')

    # return (rounds, moves) 

def ai_user_game(board_length, ship_lengths, agent_name = 'Naive', width = 300, height = 300, print_move = True, display = True, sleep=None, summary = True)
    pass 
        
def main():
    board_length = 5
    # board_length = int(input('Enter length of board: '))
    ship_lengths = (1, 2)
    agent_name = 'Naive'
    width = 600
    height = 600
    print_move = False
    display = True
    sleep = None
    summary = True
    solo_game(board_length = board_length, 
         ship_lengths = ship_lengths, 
         agent_name = agent_name,
         width = width,
         height = height,
         print_move = print_move,
         display = display,
         sleep = sleep,
         summary = summary)


if __name__ == '__main__':
    main() 