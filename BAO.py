# -*- coding: utf-8 -*-
"""
BAO...
"""
from BAO_functions import printing
from BAO_functions import turn

# Set up players and board
p1_board = [2] * 16
p2_board = [2] *16 
hand = 0

p1_board,p2_board = turn(p1_board, p2_board, 1)

# Print
printing(p1_board, p2_board, hand, 0)
   

