import Initialize, AuxiliaryFunctions

black_win = True
white_win = False
draw = False

white_turn = True
black_turn = not white_turn
while not (white_win or black_win or draw):
    move = input()
print(AuxiliaryFunctions.algebraic_notation_to_tuple("A5"))