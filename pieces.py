import board_utils as b_utils
"""Just defines pieces possible moves and attacks"""
class Piece():
    def __init__(self, x, y, color):
        """Builds a piece.

        Keyword arguments:
        x --
        y --
        color -- either "B" or "W"
            """
        self.x = x
        self.y = y
        self.color = color


    def possibleMoves(self):
        return [(self.x,self.y)]

    def possibleAttacks(self):
        return []

    def currentPos(self):
        return (self.x, self.y)

class Pawn(Piece):
    def possibleMoves(self):
        moves = []
        if self.color == "B": # black pawn moves from up to down
            move = (self.x, self.y + 1)
            if b_utils.is_inside_board(move): moves.append(move)
        else:
            move = (self.x, self.y - 1)
            if b_utils.is_inside_board(move): moves.append(move)
        return moves

    def possibleAttacks(self):
        attacks = []
        if self.color == "B":
            attack = (self.x - 1, self.y+1)
            if b_utils.is_inside_board(attack): attacks.append(attack)
            attack = (self.x + 1, self.y+1)
            if b_utils.is_inside_board(attack): attacks.append(attack)
        else:
            attack = (self.x - 1, self.y - 1)
            if b_utils.is_inside_board(attack): attacks.append(attack)
            attack = (self.x + 1, self.y - 1)
            if b_utils.is_inside_board(attack): attacks.append(attack)
        return attacks

class Bishop(Piece):
    def possibleMoves(self):
        moves = []
        x, y = self.x+1, self.y+1
        while b_utils.is_inside_board((x,y)):
            moves.append((x,y))
            x += 1
            y += 1
        x, y = self.x + 1, self.y - 1
        while b_utils.is_inside_board((x, y)):
            moves.append((x, y))
            x += 1
            y -= 1
        x, y = self.x - 1, self.y - 1
        while b_utils.is_inside_board((x, y)):
            moves.append((x, y))
            x -= 1
            y -= 1
        x, y = self.x - 1, self.y + 1
        while b_utils.is_inside_board((x, y)):
            moves.append((x, y))
            x -= 1
            y += 1
        return moves

    def possibleAttacks(self):
        return self.possibleMoves()


#Testing
if __name__ == "__main__":
    print("Testing PAWNS")
    pawn = Pawn(3, 3, "B")
    print(pawn.possibleAttacks())
    print(pawn.possibleMoves())

    print("Testing Bishop")
    bishop = Bishop(0,0, "B")
    print(bishop.possibleMoves())
    bishop = Bishop(7, 7, "B")
    print(bishop.possibleMoves())
    bishop = Bishop(3, 3, "B")
    print(bishop.possibleMoves()) # should be equal to [(4, 4), (5, 5), (6, 6), (7, 7), (4, 2), (5, 1), (6, 0), (2, 2), (1, 1), (0, 0), (2, 4), (1, 5), (0, 6)]