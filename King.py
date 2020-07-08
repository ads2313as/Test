from Piece import *

class King(Piece):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, cells):
        moves = [(self.x + 1, self.y - 1), (self.x + 1, self.y), (self.x + 1, self.y + 1), # right to the king
                 (self.x, self.y - 1), (self.x, self.y + 1), # above and below king
                 (self.x - 1, self.y - 1), (self.x - 1, self.y), (self.x - 1, self.y + 1) # left to the king
                ]

        for item in moves2:
            if not (item[0] > 8 or item[0] < 1 or item[1] > 8 or item[0] < 1):
                moves.append(item)
        return moves