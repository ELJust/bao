# -*- coding: utf-8 -*-
"""
BAO...
"""
from BAO_functions import printing

# Set up players and board
p1_board = [2] * 16
p2_board = [2] *16

p1_board[0] = 0
hand1 = 0
hand2 = 0

# Print
print(printing(p1_board, p2_board, hand1, hand2))


def add_value(p1_board, hand1):
    

    return hand1


# Define the empty move
def empty_1(p1_board, hand1):
    """ hand1 = hand1 + p1_board[i]
    p1_board[i] = 0
    """
    output = add_value(p1_board, hand1)
    p1_board[0] = 0

    return output

#Try
result = empty_1(p1_board, hand1)
print('Player One Board:', p1_board)
print('Player One Hand:', hand1)

# Define move
def move(p1_board, hand1):
    """ while hand1 >0: i+1 += 1 and 
    hand1 = hand1 - 1
    for hand1 = 0:
        if p1_board[i] > 1: eat
        else: player2's turn!
    """
    return    

 # Define Eat move 
def eat_2(p1_board, hand1):
    """ if p1_board[i] >= 1 and 
    p1_board[i_gegenüber]>=1:
        empty
    else: move    
    """
    # say I land in the first hole
    if p1_board[0] >= 1 and p1_board[15] >= 1:
        empty_1(p1_board, hand1)
    else:
        move(p1_board, hand1)
    return

# Try out 
result = eat_2(p1_board, hand1)
print('Player One Board:', p1_board)
print('Player One Hand:', hand1)