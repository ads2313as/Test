from tkinter import Tk, Frame, Canvas
import math

"""Used for board size."""
HEIGHT, WIDTH = 500, 500
"""Used for determining cell colour."""
BLACK_BOARD, WHITE_BOARD = "#2b9466", "#84e0cb"
root = Tk()




def draw_empty_board(canvas):
    x0, y0 = 0, 0
    padding = 2
    xh = math.floor(HEIGHT/8)
    yh = math.floor(WIDTH/8)
    n = 1
    for i in range(8):
        y0 = i * yh + padding
        for j in range(8):
            x0 = j*xh + padding
            canvas.create_rectangle(x0,y0,x0+xh,y0+yh,fill=BLACK_BOARD if n % 2 == 0 else WHITE_BOARD)
            n += 1
        n += 1


board = Canvas(height=HEIGHT, width=WIDTH)
draw_empty_board(board)
board.pack()

root.mainloop()