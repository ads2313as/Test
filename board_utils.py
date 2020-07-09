def is_inside_board(move):
    if(move[0] >= 0 and move[1] >= 0 and move[0] <= 7 and move[1] <= 7): return True
    return False
