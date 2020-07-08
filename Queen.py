from Piece import *


class Queen(Piece):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, cells):
        moves = []
        i = 1
        while self.x - i > 0 and self.y - i > 0:
            moves.append(self.x - i, self.y - i)  # /<
            i += 1

        i = 1
        while self.x - i > 0 and self.y + i < 9:
            moves.append(self.x - i, self.y + i)  # \<
            i += 1

        i = 1
        while self.x + i < 9 and self.y - i > 0:
            moves.append(self.x + i, self.y - i)  # \>
            i += 1

        i = 1
        while self.x + i < 9 and self.y + i < 9:
            moves.append(self.x + i, self.y + i)  # />
            i += 1

        for i in [j for j in range(1, 9) if j != self.x]:
            moves.append(self.x, i)
            moves.append(i, self.y)

        return moves