from Grid import Grid
from Square import Square


class GameBoard:
    grid = Grid(1, 8, 1, 8)
    color_1 = None
    color_2 = None

    def __init__(self, color_1, color_2):
        self.grid.set_host(self)
        self.init_grid_colors(color_1, color_2)

    def load_grid(self, squares):
        self.grid.put(squares)

    def init_grid_colors(self, color_1, color_2):
        switch = 1
        for array in self.grid.squares:
            for square in array:
                if switch == 1:
                    square.set_color(color_1)
                else:
                    square.set_color(color_2)
                switch = switch * (-1)

    def switch_x(self, argument):
        switcher = {
            1: 'A',
            2: 'B',
            3: 'C',
            4: 'D',
            5: 'E',
            6: 'F',
            7: 'G',
            8: 'H',
        }
        return switcher.get(argument)

    def forward(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if y != 8:
            return self.get_grid().square_up(x, y)
        else:
            return None

    def back(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if y != 1:
            return self.get_grid().square_down(x, y)
        else:
            return None

    def left(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if x != 1:
            return self.get_grid().square_left(x, y)
        else:
            return None

    def right(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if x != 8:
            return self.get_grid().square_right(x, y)
        else:
            return None

    def forward_right(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if y != 8 and x != 8:
            return self.get_grid().square_up_right(x, y)
        else:
            return None

    def forward_left(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if y != 8 and x != 1:
            return self.get_grid().square_up_left(x, y)
        else:
            return None

    def back_right(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if y != 1 and x != 8:
            return self.get_grid().square_down_right(x, y)
        else:
            return None

    def back_left(self, square):
        x = self.switch_x(square.get_x())
        y = square.get_y()
        if y != 1 and x != 1:
            return self.get_grid().square_down_left(x, y)
        else:
            return None

    def get_color_1(self):
        return self.color_1

    def get_color_2(self):
        return self.color_2

    def get_grid(self):
        return self.grid

    def is_color_1(self, piece):
        if piece.get_color() == self.get_color_1():
            return True
        else:
            return False

    def is_color_2(self, piece):
        if piece.get_color() == self.get_color_2():
            return True
        else:
            return False

    def place(self, piece, square):
        square.set_occupant(piece)
        piece.set_square(square)

    def get_square(self, char, y):
        x = self.switch_x(char)
        return self.get_grid().get_x_y(x, y)

    def forward_left_all(self, square):
        squares = []
        while self.forward_left(square) is not None:
            squares.append(self.forward_left(square))
        return squares

    def forward_right_all(self, square):
        squares = []
        while self.forward_right(square) is not None:
            squares.append(self.forward_right(square))
        return squares

    def back_left_all(self, square):
        squares = []
        while self.back_left(square) is not None:
            squares.append(self.back_left(square))
        return squares

    def back_right_all(self, square):
        squares = []
        while self.back_right(square) is not None:
            squares.append(self.back_right(square))
        return squares

    def forward_all(self, square):
        squares = []
        while self.forward(square) is not None:
            squares.append(self.forward(square))
        return squares

    def back_all(self, square):
        squares = []
        while self.back(square) is not None:
            squares.append(self.back(square))
        return squares

    def right_all(self, square):
        squares = []
        while self.right(square) is not None:
            squares.append(self.right(square))
        return squares

    def left_all(self, square):
        squares = []
        while self.left(square) is not None:
            squares.append(self.left(square))
            return squares
