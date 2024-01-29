import tkinter as tk
from tkinter import ttk 
from gameboard.board import Board 
# import control.cycle as cycle 

class Field(tk.Tk):
    def __init__(self, width, height, board, padx = 1, pady = 1, minsize=30, minheight=10):
        super().__init__() 

        self._board = board 
        self._rows, self._cols = board.dimensions() 

        self._padx = padx 
        self._pady = pady 
        self._minsize = minsize 
        self._minsize = minsize 
        self._minheight = minheight 
        self._subsample_button = 9000 // min(width, height) 
        self._subsample_ship = 750 * min(self._rows, self._cols) // min(width, height)

        self.resizable(1, 1)
        self.title('Battleship')
        self._width = width 
        self._height = height 
        self.geometry(f'{width}x{height}')
        self._background = 'white'
        self.configure(background=self._background)
        self.ship_image = tk.PhotoImage(file = 'images/buttons/ship.png').subsample(self._subsample_ship)


    def split_screen(self, title_left='AI', title_right='You'):
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 10)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        
        fontsize = min(self._width // 10, self._height // 10)
        font = ('Arial', fontsize, 'bold')
        
        left_canvas = tk.Canvas(self, bg='lightblue', text=title_left, font=font)
        right_canvas = tk.Canvas(self, bg='lightblue', text=title_right, font=font)
        left_canvas.grid(row=0, column=0, sticky='nsew')
        right_canvas.grid(row=0, column=1, sticky='nsew')

        screen_left = tk.Frame(self)
        screen_left.grid(row=1, column=0, sticky='nsew')
        screen_right = tk.Frame(self)
        screen_right.grid(row=1, column=1, sticky='nsew')
        return(screen_left, screen_right) 

    def field_ai(self, parent=None):
        if not parent: parent = self
        self._moves = list() 

        w = self._width // self._cols 
        h = self._height // self._rows 

        self._squares = {}
        for row in range(self._rows):
            self.rowconfigure(row, weight = 1, minsize=self._minsize)
            for col in range(self._cols):
            # TODO: Add a frame around each square Canvas so that it does not change size when resizing the window -> Ship and red X stay in the middle
                self.columnconfigure(col, weight = 1, minsize=self._minsize)
                color = 'black'
                square = tk.Canvas(master=parent, width=w, height=h, bg=color)
                square.grid(row=row, column=col, padx = self._padx, pady = self._pady, sticky = 'nsew') 
                self._squares[(row, col)] = square 
    
    def buttons(self, parent=None):
        if not parent: parent = self
        buttons = tk.Frame(parent)
        grid_row = parent.grid_size()[1]
        buttons.grid(row=grid_row, column=0, columnspan=self._cols, sticky='nswe')
        buttons.rowconfigure(0, weight = 1, minsize=self._minheight)
        for i in range(3): buttons.columnconfigure(i, weight=1, minsize=self._minsize)

        rest_img = tk.PhotoImage(file='images/buttons/reload.png').subsample(self._subsample_button)
        prev_img = tk.PhotoImage(file='images/buttons/back.png').subsample(self._subsample_button)
        next_img = tk.PhotoImage(file='images/buttons/next.png').subsample(self._subsample_button)

        button_rest = tk.Button(buttons, text = 'Restart', command=self.restart, image = rest_img, compound = tk.LEFT)
        button_rest.image = rest_img
        button_rest.grid(row=0, column=0, padx = self._padx, pady = self._pady, sticky='nwse')

        button_prev = tk.Button(buttons, text = 'Previous', command=self.prev_move, image = prev_img, compound = tk.LEFT)
        button_prev.image = prev_img
        button_prev.grid(row=0, column=1, padx = self._padx, pady = self._pady, sticky='nwse')

        button_next = tk.Button(buttons, text='Next', command=self.next_move, image = next_img, compound = tk.LEFT)
        button_next.image = next_img
        button_next.grid(row=0, column=2, padx = self._padx, pady = self._pady, sticky='nwse')



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
        cur_square = self._squares[row, col] 
        x = cur_square.winfo_width() // 2
        y = cur_square.winfo_height() // 2
        font = int(min(x, y)) 
        cur_square.configure(bg='white')
        if self._board.hit(row, col):
            cur_square.create_image(x, y, image=self.ship_image, anchor=tk.CENTER)
        # else: 
        #     img = 
        cur_square.create_text(x, y, text='X', font=('Arial', font), fill='red', anchor=tk.CENTER) 