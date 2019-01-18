# -*- coding: utf-8 -*-
"""
These are the functions for the basic game.
"""

from board import print_field
from strategies import random_start
import csv



def eat(i, opponent_board):
    """ Assign two opposing holes to each front-row hole of the current
    board.
    Eat the pebbles of the opponent, iff both of the two opposing holes 
    are filled. 
    """
    opp1 = 7-i
    opp2 = 8+i

    add_to_hand = 0
    if i >= 0 and i <= 7:
        if opponent_board[opp1] > 0 and opponent_board[opp2] > 0:
            add_to_hand = opponent_board[opp1] + opponent_board[opp2]
            opponent_board[opp1] = 0
            opponent_board[opp2] = 0

    return add_to_hand


def turn(current_board, opponent_board, start):
    hand = 0
    
    """ Start by putting all pebbles of a given hole into
    the hand """
    hand += current_board[start]
    current_board[start] = 0
    i = start 
    
    """ To move, put one pebble from hand into the neighbouring
    hole of the current board, until it is empty. 
    If the last pebble from hand is put into a hole where there is at least one
    pebble, put all into the hand plus the value from the opponent, if 
    applicable. Continue moving.
    """
    while hand > 0:
        while hand > 0:
            i = (i + 1) % 16
            current_board[i] += 1
            hand -= 1
        if current_board[i] > 1:
            hand += current_board[i]
            current_board[i] = 0 
            hand += eat(i, opponent_board)
    

def pebbles_left(board):
    """ Check how many pebbles are left on a given board.
    """
    sum_pebbles = 0
    for i in range(16):
        sum_pebbles += board[i]
    
    return sum_pebbles

def game(p1_board, p2_board):
    turn_count = 0
    while pebbles_left(p1_board) > 5 and pebbles_left(p2_board) > 5:
        turn(p1_board, p2_board, random_start(p1_board))
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

