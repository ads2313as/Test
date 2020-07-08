from Piece import *

class Pawn(Piece):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, cells):
        moves = []
        if self.y == 2: # if at 2nd rank
            moves.append((self.x, self.y + 2)) # 2 squares forward
        moves.append((self.x, self.y + 1)) # 1 square forward
        moves.apepnd((self.x + 1, self.y + 1), (self.x - 1, self.y + 1))
        return moves