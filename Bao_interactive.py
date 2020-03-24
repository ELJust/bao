# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 09:15:47 2020

@author: Eva
"""

"""
Run an interactive game of BAO.
"""


from BAO_functions import turn
from BAO_functions import pebbles_left
from board import print_field
from board import game_area
from strategies import *
from save import result_to_file


def play_game(strategy_p1, strategy_p2, max_allowed_turn_count):
    """
    The players take turns until one player has 5 or less pebbles left 
    on their board.
    Stop if the game takes too long.
    """
    p1_board = game_area()
    p2_board = game_area()
    outcome = None
    turn_count = 0
    text = ""
    
    print(print_field(p1_board, p2_board))
    while pebbles_left(p1_board) > 5 and pebbles_left(p2_board) > 5 and turn_count < max_allowed_turn_count:
        turn(p1_board, p2_board, strategies(strategy_p1, p1_board, p2_board))
        print(print_field(p1_board, p2_board))
        turn(p2_board, p1_board, strategies(strategy_p2, p2_board, p1_board))
        print(print_field(p1_board, p2_board))
        turn_count += 1

        if pebbles_left(p1_board) > 5:
            winning_player = 1
            text = ("Player 1 won the game after %d turns." % turn_count)
        if pebbles_left(p2_board) >5:
            winning_player = 2
            text = ("Player 2 won the game after %d turns." % turn_count)
    if turn_count == 100:
        winning_player = 0
        print("Too many turns!")


    print(text)
    outcome = ({'Winner': winning_player, 'turn count': turn_count})
    
    return outcome

play_game(1, 5, 100)