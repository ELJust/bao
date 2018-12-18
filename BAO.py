# -*- coding: utf-8 -*-
"""
BAO...
"""
from BAO_functions import print_field
from BAO_functions import turn
from BAO_functions import pebbles_left


# Set up players and board
p1_board = [2] * 16
p2_board = [2] *16 
hand = 0


def game(p1_board, p2_board):
    while pebbles_left > 5:
        turn(p1_board, p2_board, 0)
        print_field(p1_board, p2_board, hand, 0)
        turn(p2_board, p1_board, 0)
        print_field(p1_board, p2_board, hand, 0)
    print("Game Over.")

game(p1_board, p2_board)
# To Do: 
# Overall Game    
#define start /strategy
# Game Over message :)
        