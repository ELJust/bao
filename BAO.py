# -*- coding: utf-8 -*-
"""
BAO...
"""

# Set up players and board

p1_board = [2] * 16
p2_board = [2] *16

hand1 = 0
hand2 = 0

# Print status of the game
print('Player One Board:', p1_board)
print('Player One Hand:', hand1)
print('Player Two Board:', p2_board)
print('Player Two Hand:', hand2)

# Define the different moves
def empty_1(p1_board, hand1):
    # Say I start at the first whole
    # maybe try the for loop -- not working
    for number in p1_board :
        hand1 += p1_board[1] 
    p1_board[1] = 0

    return

# Try out the different moves
result = empty_1(p1_board, hand1)
print('Player One Board:', p1_board)
print('Player One Hand:', hand1)  
