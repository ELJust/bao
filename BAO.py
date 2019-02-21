# -*- coding: utf-8 -*-
"""
Run a game of BAO.
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
    
    while pebbles_left(p1_board) > 5 and pebbles_left(p2_board) > 5 and turn_count < max_allowed_turn_count:
        turn(p1_board, p2_board, strategies(strategy_p1, p1_board, p2_board))
        #print(print_field(p1_board, p2_board))
        turn(p2_board, p1_board, strategies(strategy_p2, p1_board, p2_board))
        #print(print_field(p1_board, p2_board))
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

def play_multiple_games(strategy_p1, strategy_p2, max_allowed_turn_count, times):
    wins_p1 = 0
    wins_p2 = 0
    turns_p1 = 0
    turns_p2 = 0
    avg_wins_p2 = 0
    avg_wins_p1 = 0
    avg_turn_count_p1 = 0
    avg_turn_count_p2 = 0
    for i in range(times):
        results = play_game(strategy_p1, strategy_p2, max_allowed_turn_count)
        #result_to_file('results_max_vs_random.csv', results)
        if results['Winner'] == 1:
            wins_p1 += 1
            turns_p1 += results['turn count']
        if results['Winner'] == 2:
            wins_p2 += 1
            turns_p2 += results['turn count']
    avg_wins_p1 = wins_p1/100
    avg_wins_p2 = wins_p2/100
    if wins_p1 != 0:
        avg_turn_count_p1 = turns_p1/wins_p1
    if wins_p2 != 0:
        avg_turn_count_p2 = turns_p2/wins_p2
    ties = times - wins_p1 - wins_p2
    
    print("Player 1 won on average {} times after an average of {} turns. \nPlayer 2 won on average {} times after an average of {} turns. \nPlayers tied {} times.".format(avg_wins_p1, avg_turn_count_p1, avg_wins_p2, avg_turn_count_p2, ties))


play_multiple_games(2, 1, 100, 1000)
        