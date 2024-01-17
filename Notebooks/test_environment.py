from environment import Board  

ships = list() 
ship_1 = {"col": 0, "row": 0, "length": 3, "vertical": True} 
ship_2 = {"col": 2, "row": 1, "length": 2, "vertical": False}
ship_3 = {"col": 2, "row": 3, "length": 4, "vertical": True} 
ship_4 = {"col": 0, "row": 0, "length": 3, "vertical": True} 
ship_5 = {"col": -1, "row": 0, "length": 3, "vertical": True} 
ship_6 = {"col": 0.5, "row": 0, "length": 3, "vertical": True} 

ships.append(ship_1) # Should work 
# ships.append(ship_2) # Raise ValueError (Boat touching)
# ships.append(ship_3) # Raise ValueError (borders)
# ships.append(ship_4) # Raise ValueError (overlapping)
# ships.append(ship_5) # Raise ValueError (coordinates)
# ships.append(ship_6) # Raise ValueError (coordinates)

board = Board(5, ships)