ranks = {"A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8
              }
pieces = {"B": Bishop,
          "Q": Queen,
          "K": King,
          "N": Knight,
          "R": Rook





}
def algebraic_notation_to_tuple(move): # input, ex. "A5", ...
    move = list(move)
    return ranks[move[0]], int(move[1])

def recognize_piece(move):
    move = list(move)
