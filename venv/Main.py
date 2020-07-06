'''from test import show_board, is_syntax_valid_move
import Pawn, King
import re
'''
starting_board=[  ['r','n','b','q','k','b','n','r'],
                ['p','p','p','p','p','p','p','p'],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                [' ',' ',' ',' ',' ',' ',' ',' '],
                ['P','P','P','P','P','P','P','P'],
                  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
current_board=starting_board


white_win=False
black_win=False
'''while not (black_win or white_win):
    show_board(current_board)
    move=input()
    white_to_move=True
    Pawn.possible_moves(current_board, move, white_to_move)
    white_win=True
'''
counter=0
for i in range(1,2020):
  for j in range(1,2020):
      for k in range(1,2020):
        if i + j > k:
          if j + k>i:
            if i +k >j:
              if i**2+j**2==k**2 or i**2+k**2==j**2 or k**2+j**2==i**2:
                counter+=1
print(counter)