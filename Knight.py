import Piece


class Knight(Piece):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def possible_moves(self, cells):
        moves = []
        moves2 = [(self.x - 1, self.y - 2), (self.x - 1, self.y + 2),
                  (self.x + 1, self.y - 2), (self.x + 1, self.y + 2),
                  (self.x - 2, self.y - 1), (self.x - 2, self.y + 1),
                  (self.x + 2, self.y - 1), (self.x + 2, self.y + 1)
                  ]
        for item in moves2:
            if not( item[0] > 8 or item[0] < 1 or item[1] > 8 or item[0] < 1):
                moves.append(item)
        return moves
