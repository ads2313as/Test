import Piece


class Bishop(Piece):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, cells):
        moves = []
        i = 1
        while self.x - i > 0 and self.y - i > 0:
            moves.append(self.x - i, self.y - i) # /<
            i+=1

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

        return moves



