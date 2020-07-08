class piece:
    def __init__(self, x, y, color, type):
        """Builds a piece.

        Keyword arguments:
        x --
        y --
        color -- either "B" or "W"
        type -- Any from "B",
            """
        self.x = x
        self.y = y
        self.color = color
        self.type = type