class Cell:
    x = None
    y = None
    piece = None

    def __init__(self, x, y, piece):
        self.set_piece(piece)
        self.set_x(x)
        self.set_y(y)

    def set_piece(self, piece):
        self.piece = piece

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def return_piece(self):
        return self.piece

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

