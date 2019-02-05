# -*- coding: utf-8 -*-
"""
Run a game of BAO.
"""
from BAO_functions import turn
from BAO_functions import pebbles_left
from board import print_field
from strategies import random_start
from strategies import max_pebbles_start
from strategies import min_pebbles_start
from strategies import maxmin_start


def game(p1_board, p2_board):
    """
    The players take turns until one player has 5 or less pebbles left 
    on their board.
    """
    turn_count = 0
    print_field(p1_board, p2_board)
    
    while pebbles_left(p1_board) > 5 and pebbles_left(p2_board) > 5:
        turn(p1_board, p2_board, maxmin_start(p1_board, p2_board))
        print_field(p1_board, p2_board) 
        turn(p2_board, p1_board, random_start(p2_board))
        print_field(p1_board, p2_board)
        turn_count += 1
        
        if pebbles_left(p1_board) > 5:
            winning_player = 1
        if pebbles_left(p2_board) >5:
            winning_player = 2
            
    print("Game Over. Player %d won." % winning_player)
    print("Overall turns taken:", turn_count)


p1_board = [2] * 16
p2_board = [2] * 16 
hand = 0
game(p1_board, p2_board)
    # store/append result in a csv file
     
# To Do:     
#define strategies
# define save
#def save_results():
