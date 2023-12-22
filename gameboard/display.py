import tkinter as tk
from tkinter import ttk 
from environment import Board 

class Field(tk.Tk):
    def next_move(self):
        if not len(self._moves):
            self.destroy()
        else: 
            move = self._moves.pop(0) 
            self.update(*move)
            if self.print_move: print(move) 
        self.update_idletasks() 

    def __init__(self, width, height, board):
        super().__init__() 
        self._width = width 
        self._height = height 
        self._board = board 

        self.title("Battleship")
        self.geometry(f"{width}x{height}")
        self._rows, self._cols = board.dimensions() 
        self._moves = list() 

        w = self._width // self._cols 
        h = self._height // self._rows 

        self._frame = tk.Frame(master=self) 
        self._frame.pack() 
        self._squares = {}
        for row in range(self._rows):
            self.rowconfigure(row, weight = 1, minsize=50)
            for col in range(self._cols - 1):
            # TODO: Adjust the number of col range later 
            # for col in range(self._cols):
                self.columnconfigure(col, weight = 1, minsize=50)
                color = "white" if row % (col + 1) == 1 else "black"
                square = tk.Canvas(master=self._frame, width=w, height=h, bg=color, borderwidth=0, highlightthickness=0)
                square.grid(row=row, column=col) 
                self._squares[(row, col)] = square 

        # TODO: Delete later, for test purposes only 
        # TODO: Adjust the position of the Button 
        tk.Button(self._frame, text="Next", command=self.next_move).grid(row=9, column=9)

    def run_game(self, moves, print_move):
        self._moves = moves 
        self.print_move = print_move
        self.mainloop() 

    # TODO: Show the location of the boats 
    def uncover(self, ships):
        for row in range(self._rows):
            for col in range(self._cols - 1):
            # TODO: Adjust the number of col range later 
            # for col in range(self._cols):  
                pass

    def update(self, row, col):
        x = self._width // self._cols / 2
        y = self._height // self._rows / 2
        
        font = int(min(x, y)) 
        w = self._width // self._cols 
        h = self._height // self._rows 
        new_square = tk.Canvas(master=self._frame, width=w, height=h, bg="white", borderwidth=0, highlightthickness=0) 
        new_square.create_text(x, y, text="X", font=("Arial", font), fill="red") 
        self._squares[(row, col)] = new_square 
        new_square.grid(row=row, column=col)