from . import Piece
from Move import Move


class Knight(Piece.Piece):
    def __init__(self, player, starting_square):
        super().__init__(player, starting_square)
        self.name = 'KNIGHT'

    def possible_moves(self):
        moves_list = list(Move)
        # the forward squares
        temp_square = self.get_board().forward(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().forward(temp_square)
            # add left and right
            if temp_square is not None:
                moves_list.append(self.get_board().left(temp_square))
                moves_list.append(self.get_board().right(temp_square))
        # the back squares
        temp_square = self.get_board().back(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().back(temp_square)
            if temp_square is not None:
                # add left and right
                moves_list.append(self.get_board().left(temp_square))
                moves_list.append(self.get_board().right(temp_square))
        # The right squares
        temp_square = self.get_board().right(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().right(temp_square)
            if temp_square is not None:
                # add forward and back
                moves_list.append(self.get_board().forward(temp_square))
                moves_list.append(self.get_board().back(temp_square))
        # The left squares
        temp_square = self.get_board().left(self.get_square())
        if temp_square is not None:
            temp_square = self.get_board().left(temp_square)
            if temp_square is not None:
                # add forward and back
                moves_list.append(self.get_board().forward(temp_square))
                moves_list.append(self.get_board().back(temp_square))
        return moves_list
