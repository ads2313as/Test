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


#Testing
if __name__ == "__main__":
    pawn = Pawn(3, 3, "B")
    print(pawn.possibleAttacks())
    print(pawn.possibleMoves())