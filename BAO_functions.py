# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 14:37:19 2018

@author: Eva
"""
# Return current status of board, including hand
def printing(p1_board, p2_board, hand1, hand2):
    print('-------------- Player One --------------')
    print('Pebbles in hand:' , hand1)
    print('-----------------------------------------')
    print('|' , p1_board[8], '||', p1_board[9], '||',
      p1_board[10], '||', p1_board[11], '||', p1_board[12],
      '||', p1_board[13], '||', p1_board[14], '||', p1_board[15],
      '|' )
    print('-----------------------------------------')
    print('|' , p1_board[7], '||', p1_board[6], '||',
      p1_board[5], '||', p1_board[4], '||', p1_board[3],
      '||', p1_board[2], '||', p1_board[1], '||', p1_board[0],
      '|')
    print('-----------------------------------------')
    print('-----------------------------------------')
    print('|' , p2_board[0], '||', p2_board[1], '||',
      p2_board[2], '||', p2_board[3], '||', p2_board[4],
      '||', p2_board[5], '||', p2_board[6], '||', p2_board[7],
      '|' )
    print('-----------------------------------------')
    print('|' , p2_board[15], '||', p2_board[14], '||',
      p2_board[13], '||', p2_board[12], '||', p2_board[11],
      '||', p2_board[10], '||', p2_board[9], '||', p2_board[8],
      '|')
    print('-----------------------------------------')
    print('Pebbles in hand:', hand2)
    print('-------------- Player Two --------------')

# Assign two opposing holes to each hole of the current board
def opposing(current_board, opponent_board):
    if current_board[0]:
        opp1 = opponent_board[7] 
        opp2 = opponent_board[8]
    if current_board[1]:
        opp1 = opponent_board[6]
        opp2 = opponent_board[9]
    if current_board[2]:
        opp1 = opponent_board[5]
        opp2 = opponent_board[10]
    if current_board[3]:
        opp1 = opponent_board[4] 
        opp2 = opponent_board[11] 
    if current_board[4]:
        opp1 = opponent_board[3] 
        opp2 = opponent_board[12]
    if current_board[5]:
        opp1 = opponent_board[2]
        opp2 = opponent_board[13]
    if current_board[6]:
        opp1 = opponent_board[1]
        opp2 = opponent_board[14]
    if current_board[7]:
        opp1 = opponent_board[0] 
        opp2 = opponent_board[15]

    return opp1, opp2

# Define how a turn works
def turn(current_board, opponent_board, start):
    hand = 0
    
    """ Start by putting all pebbles of a given hole into
    the hand """
    hand += current_board[start]
    current_board[start] = 0
    i = start 
    
    """ To move put one pebble from hand into the neighbouring
    hole of the current board"""
    while hand > 0:
        while hand > 0:
            i = (i + 1) % 16
            current_board[i] += 1
            hand -= 1
        if current_board[i] > 1:
            hand += current_board[i]
            current_board[i] = 0 
            if opp1[i] > 0 and opp2[i] > 0:
                hand += opp1[i] + opp2[i]
                opp1[i] = 0
                opp2[i] = 0

    
    return current_board, opponent_board