# -*- coding: utf-8 -*-
"""
BAO...
"""
from BAO_functions import print_field
from BAO_functions import turn


# Set up players and board
p1_board = [2] * 16
p2_board = [2] *16 
hand = 0

# Do a turn where p1_board is the current_board
turn(p1_board, p2_board, 1)

# Print
print_field(p1_board, p2_board, hand, 0)
   
turn(p2_board, p1_board, 1)

#def game(current_board, opponent_board):
#while opponent_board insg >= 5:
 #   turn
#print(*player x won!)