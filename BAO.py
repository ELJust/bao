# -*- coding: utf-8 -*-
"""
Run a game of BAO.
"""
from BAO_functions import turn
from BAO_functions import pebbles_left
from board import print_field
from strategies import *
from save import *


def game(p1_board, p2_board):
    """
    The players take turns until one player has 5 or less pebbles left 
    on their board.
    Stop if the game takes too long.
    """
    outcome = None
    turn_count = 0
    #print_field(p1_board, p2_board)
    
    while pebbles_left(p1_board) > 5 and pebbles_left(p2_board) > 5 and turn_count < 100:
        turn(p1_board, p2_board, min_pebbles_start(p1_board, p2_board))
        #print_field(p1_board, p2_board) 
        turn(p2_board, p1_board, random_start(p2_board))
        #print_field(p1_board, p2_board)
        turn_count += 1
        
        if pebbles_left(p1_board) > 5:
            winning_player = 1
        if pebbles_left(p2_board) >5:
            winning_player = 2
    if turn_count == 100:
        winning_player = 0
        print("Too many turns!")
            
    print("Game Over. Player %d won." % winning_player)
    print("Overall turns taken:", turn_count)

    outcome = ({'Winner': winning_player, 'turn count': turn_count})
    
    return outcome


for i in range(0, 100):
    p1_board = [2] * 16
    p2_board = [2] * 16 
    hand = 0
    result = game(p1_board, p2_board)
    print(p1_board)
    print(p2_board)
    print(i)
    result_to_file('results_min3.csv', result)

