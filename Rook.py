from Piece import *


class Rook(Piece):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, cells):
        moves = []
        for i in [j for j in range(1, 9) if j != self.x]:
            moves.append(self.x, i)
            moves.append(i, self.y)
        return moves
