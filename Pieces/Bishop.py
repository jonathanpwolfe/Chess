from . import Piece
from Move import Move


class Bishop(Piece.Piece):
    def __init__(self, player, starting_square):
        super.__init__(player, starting_square)
        self.name = 'BISHOP'

    def possible_moves(self):
        moves_list = list(Move)
        moves_list.append(self.get_board().forward_left_all(self.get_square()))
        moves_list.append(self.get_board().forward_right_all(self.get_square()))
        moves_list.append(self.get_board().back_left_all(self.get_square()))
        moves_list.append(self.get_board().back_right_all(self.get_square()))
        return moves_list

    def valid_moves(self):
        moves_list1 = self.possible_moves()
        moves_list2 = list(Move)
