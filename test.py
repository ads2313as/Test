import re

'''
def show_board(current_board):  # wyswietlanie szachownicy
    row_counter = 8
    print('-'*33)
    for item in current_board:
        for i in item:
            print("| {}".format(i), end=' ')
        print('| {}'.format(row_counter))
        row_counter -= 1
        print('-'*33)
    for letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        print("  {} ".format(letter), end='')
    print('')


def is_syntax_valid_move(move):  # sprawdzanie czy dobry ruch w sensie składniowym
    move_pattern = r'[p,P,k,K,q,Q,b,B,n,N,r,R,'']{0,1}[a-hA-H][1-8]'
    if len(re.findall(move_pattern, move))!=0:
        return True  # valid move
    else:
        return False  # invalid move
    # testing every move
    for piece in ['p','P','k','K','q','Q','b','B','n','N','r','R','']:
        for letter in ['a','b','c','d','e','f','g','h','A','B','C','D','E','F','G','H']:
            for number in range(1, 9):
                moves = r'{}{}{}'.format(piece, letter, number)
                print(moves)
                print(re.findall(move_pattern, moves))'''


import matplotlib.pyplot as plt, random
from scipy import special

z = [random.random()**2 for i in range(1010)]
#z=sorted(z)
y=[i for i in range(1010)]
#x=[random.uniform(0,1) for i in range(1000)]
#x=sorted(x)
plt.scatter(y,z)
plt.show()
