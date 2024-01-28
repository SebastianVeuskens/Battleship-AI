import tkinter as tk
from tkinter import ttk 
from gameboard.board import Board 
# import control.cycle as cycle 

class Field(tk.Tk):
    def __init__(self, width, height, board, padx = 1, pady = 1, minsize=30, min_height=10):
        super().__init__() 
        self.resizable(1, 1)
        self.title('Battleship')
        self._width = width 
        self._height = height 
        self.geometry(f'{width}x{height}')
        self._background = 'white'
        self.configure(background=self._background)

        self._board = board 
        self._rows, self._cols = board.dimensions() 
        self._moves = list() 

        w = self._width // self._cols 
        h = self._height // self._rows 

        # self._frame = tk.Frame(master=self) 
        # self._frame.pack() 
        self._squares = {}
        for row in range(self._rows):
            self.rowconfigure(row, weight = 1, minsize=minsize)
            for col in range(self._cols):
            # TODO: Adjust the number of col range later 
            # for col in range(self._cols):
                self.columnconfigure(col, weight = 1, minsize=minsize)
                color = 'white' if row % (col + 1) == 1 else 'black'
                square = tk.Canvas(master=self, width=w, height=h, bg=color)
                square.grid(row=row, column=col, padx = padx, pady = pady, sticky = 'nsew') 
                self._squares[(row, col)] = square 

        buttons = tk.Frame(self)
        buttons.grid(row = self._rows, column=0, columnspan=self._cols, sticky='nswe')
        buttons.rowconfigure(0, weight = 1, minsize=min_height)
        for i in range(3): buttons.columnconfigure(i, weight=1, minsize=minsize)

        rest_img = tk.PhotoImage(file='images/buttons/reload.png').subsample(15)
        prev_img = tk.PhotoImage(file='images/buttons/back.png').subsample(15)
        next_img = tk.PhotoImage(file='images/buttons/next.png').subsample(15)

        button_rest = tk.Button(buttons, text = 'Restart', command=self.restart, image = rest_img, compound = tk.LEFT)
        button_rest.image = rest_img
        button_rest.grid(row=0, column=0, padx = padx, pady = pady, sticky='nwse')

        button_prev = tk.Button(buttons, text = 'Previous', command=self.prev_move, image = prev_img, compound = tk.LEFT)
        button_prev.image = prev_img
        button_prev.grid(row=0, column=1, padx = padx, pady = pady, sticky='nwse')

        button_next = tk.Button(buttons, text='Next', command=self.next_move, image = next_img, compound = tk.LEFT)
        button_next.image = next_img
        button_next.grid(row=0, column=2, padx = padx, pady = pady, sticky='nwse')

    def next_move(self):
        if not len(self._moves):
            # TODO: Enable next button if game is finished instead of closing the window 
            self.button_next.state(['disabled'])
        else: 
            move = self._moves.pop(0) 
            self.update(*move)
            if self.print_move: print(move) 
        self.update_idletasks() 

    # TODO: Implement previous move. Requires change in update method. 
    def prev_move(self):
        pass 

    # TODO: Implement restart method. Might require whole change of main program, transfer into field. 
    def restart(self):
        # control.cycle.solo_game(*self.args)
        # self.destroy() 
        pass 

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
        # w = self._width // self._cols 
        # h = self._height // self._rows 
        # new_square = tk.Canvas(master=self, width=w, height=h, bg='white') 
        # new_square.create_text(x, y, text='X', font=('Arial', font), fill='red') 
        # self._squares[(row, col)] = new_square 
        # new_square.grid(row=row, column=col, padx = 5, pady = 5, sticky = 'nsew')
        cur_square = self._squares[row, col] 
        x = cur_square.winfo_width() // 2
        y = cur_square.winfo_height() // 2
        font = int(min(x, y)) 
        cur_square.create_text(x, y, text='X', font=('Arial', font), fill='red', anchor=tk.CENTER) 