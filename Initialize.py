from Piece import *
from Cell import *
from Pawn import *
from Rook import *
from Bishop import *
from Knight import *
from Queen import *
from King import *

cells = []
pieces = [Rook, Bishop, Knight, Queen, King, Knight, Bishop, Rook]
for i in range(8):
    cells.append(Cell(i + 1, 2, Pawn))  # initializing white pawns at 2nd rank
    cells.append(Cell(i + 1, 7, Pawn))  # initializing black pawns at 7th rank
    cells.append(Cell(i + 1, 1, pieces[i]))  # initializing white pieces at 1st rank
    cells.append(Cell(i + 1, 8, pieces[i]))  # initializing black pieces at 7th rank
