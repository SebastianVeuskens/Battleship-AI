import pytest 
import unittest 
import random 
import sys 
sys.path.append('G:/My Drive/Sonstiges/Projects/Battleship-AI')
import utils.exceptions as ue 
from gameboard.ship import Ship
from gameboard.board import Board 

class TestShip(unittest.TestCase):
    def test_ship(self):
        # Given length of board (random coordinate assignment)
        ship_bl_def = Ship(board_length = 10)
        ship_bl_3v = Ship(ship_length = 3, vertical = True, board_length = 10)
        ship_bl_1h = Ship(ship_length = 1, board_length = 10)

        # Assign coordinates 
        ship_cor_def = Ship(row = 3, col = 1)
        ship_cor_3v = Ship(ship_length = 3, vertical = True, row = 5, col = 1)
        ship_cor_1h = Ship(ship_length = 1, row = 2, col = 7) 

        # Ships with board length have coordinates 
        self.assertIsInstance(ship_bl_def.row, int)
        self.assertIsInstance(ship_bl_def.col, int) 

    def test_initialization(self):
        for board_length in range(5, 15):
            for _ in range(1000):
                ship = Ship(ship_length = random.randint(1, 4), board_length = board_length) 
                board = Board(board_length = board_length)
                board.place_ship(ship)
            

class TestRules(unittest.TestCase):
    def setUp(self):
        self.ship_1_1_3v = Ship(3, True, 1, 1)
        self.ship_3_6_1h = Ship(1, False, 3, 6)
        self.ship_0_7_2h = Ship(2, False, 0, 7)

        self.ship_1_05_3v = Ship(3, True, 1, 0.5)
        self.ship_m1_1_3v = Ship(3, True, -1, 1)
        self.ship_1_12_3v = Ship(3, True, 1, 12)
        self.ship_10_1_3h = Ship(3, False, 10, 1)

        self.ship_7_8_3h = Ship(3, False, 7, 8)
        self.ship_8_9_2h = Ship(2, False, 8, 9)
        self.ship_8_2_3v = Ship(3, True, 8, 2)
        self.ship_7_7_4v = Ship(4, True, 7, 7)

        self.ship_3_5_3h = Ship(3, False, 3, 5)
        self.ship_3_6_3v = Ship(3, True, 3, 6)
        self.ship_2_0_3h = Ship(3, False, 2, 0)
        self.ship_0_6_4v = Ship(4, True, 0, 6)

        self.ship_0_0_1h = Ship(1, False, 0, 0)
        self.ship_2_7_2v = Ship(2, True, 2, 7)
        self.ship_1_8_3v = Ship(3, True, 1, 8)
        self.ship_3_5_4v = Ship(4, True, 3, 5)

        self.board = Board(10)

    def test_rules(self):
        self.board.place_ship(self.ship_1_1_3v)
        self.board.place_ship(self.ship_3_6_1h)
        self.board.place_ship(self.ship_0_7_2h)

        # Basic coordinate compatibility 
        with self.assertRaises(ue.CoordinateException):
            self.board.place_ship(self.ship_1_05_3v)
        with self.assertRaises(ue.CoordinateException):     
            self.board.place_ship(self.ship_m1_1_3v)
        with self.assertRaises(ue.CoordinateException):
            self.board.place_ship(self.ship_1_12_3v)
        with self.assertRaises(ue.CoordinateException):
            self.board.place_ship(self.ship_10_1_3h)

        # Border adherence 
        with self.assertRaises(ue.BorderException):
            self.board.place_ship(self.ship_7_8_3h)            
        with self.assertRaises(ue.BorderException):
            self.board.place_ship(self.ship_8_9_2h)            
        with self.assertRaises(ue.BorderException):
            self.board.place_ship(self.ship_8_2_3v)            
        with self.assertRaises(ue.BorderException):
            self.board.place_ship(self.ship_7_7_4v)            

        # Overlapping of ships 
        with self.assertRaises(ue.OverlapException):
            self.board.place_ship(self.ship_3_5_3h)
        with self.assertRaises(ue.OverlapException):
            self.board.place_ship(self.ship_3_6_3v)
        with self.assertRaises(ue.OverlapException):
            self.board.place_ship(self.ship_2_0_3h)
        with self.assertRaises(ue.OverlapException):
            self.board.place_ship(self.ship_0_6_4v) 
            
        # Touching of ships 
        with self.assertRaises(ue.NeighbourException):
            self.board.place_ship(self.ship_0_0_1h)
        with self.assertRaises(ue.NeighbourException):
            self.board.place_ship(self.ship_2_7_2v)
        with self.assertRaises(ue.NeighbourException):
            self.board.place_ship(self.ship_1_8_3v)
        with self.assertRaises(ue.NeighbourException):
            self.board.place_ship(self.ship_3_5_4v) 
            
    

if __name__ == '__main__':
    unittest.main() 


