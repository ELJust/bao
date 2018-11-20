# -*- coding: utf-8 -*-
"""
BAO...
"""
from BAO_functions import printing
from BAO_functions import turn
from BAO_functions import opposing

# Set up players and board
p1_board = [2] * 16
p2_board = [2] *16 
hand = 0

# Do a turn where p1_board is the current_board
p1_board,p2_board = turn(p1_board, p2_board, 1)

# Print
printing(p1_board, p2_board, hand, 0)
   
# Try out the opposing holes 
current_board = [2] * 16
opponent_board = [2] * 16

opposing(current_board, opponent_board)
