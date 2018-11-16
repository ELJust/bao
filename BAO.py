# -*- coding: utf-8 -*-
"""
BAO...
"""

# Set up players and board
p1_board = [2] * 16
p2_board = [2] *16

p1_board[15] = 0
hand1 = 0
hand2 = 0

# Print status of the game
print('Player One Board:', p1_board)
print('Player One Hand:', hand1)
print('Player Two Board:', p2_board)
print('Player Two Hand:', hand2)

def add_value(p1_board, hand1):
    hand1 = 0
    output = hand1 + p1_board[0]
    return output

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
    """ while hand1 >1: i+1 += 1,
    if hand == 1: i += 1
    eat
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