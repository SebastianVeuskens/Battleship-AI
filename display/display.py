import tkinter as tk
from tkinter import ttk 
# from gameboard.environment import Board 

class Field():
    def __init__(self, width, height, board=None):
        self.width = width 
        self.height = height 

        self.window = tk.Tk()
        self.window.title("Battleship")
        self.window.geometry(f"{width}x{height}")
        self.rows, self.cols = board 
        # self.rows, self.cols = board.dimensions() 
        self.cells = list()

        for i in range(self.rows):
            self.cells.append(list()) 
            for j in range(self.cols):
                color = "white" if j % (i + 1) == 1 else "black"
                square = tk.Canvas(self.window, width=width // self.cols, height=height // self.rows, bg=color, borderwidth=0, highlightthickness=0)
                self.cells[i].append(square)
                square.grid(row=i, column=j) 
        # self.window.mainloop() 

    # TODO: Show the location of the boats 
    def uncover(self):
        pass 

    def update(self, row, col):
        x = self.width // self.cols / 2
        y = self.height // self.rows / 2
        font = int(min(x, y)) 
        self.cells[row][col].create_text(x, y, text="X", font=("Arial", font), fill="red") 