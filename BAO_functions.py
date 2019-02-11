# -*- coding: utf-8 -*-
"""
These are the functions for the basic game to run.
"""

def eat(i, opponent_board):
    """ Assign two opposing holes to each front-row hole of the current
    board.
    Eat (=take) the pebbles of the opponent, if, and only if, both of the two 
    opposing holes are filled with at least one pebble. 
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
    """ Start the turn by putting all pebbles of a given hole into
    the hand """
    hand = 0
    hand += current_board[start]
    current_board[start] = 0
    i = start 
    
    """ To move, put one pebble from hand into the neighbouring
    hole of the current board, until it is empty. 
    If the last pebble from hand is put into a hole where there is at 
    least one pebble, put all into the hand and eat the opponent's 
    pebbles, if applicable. Continue moving.
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


