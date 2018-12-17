# -*- coding: utf-8 -*-
"""
These are the functions for printing out the current status 
of the board, assigning two opposing holes for each front-row
hole, and defining how a turn works.
"""

def printing(p1_board, p2_board, hand1, hand2):
    """ Return the current status of the board, including 
    what is left in each player's hand
    """
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


def eat(i, opponent_board):
    """ Assign two opposing holes to each hole of the current
    board.
    """
   # opp1=7-i
    #opp2=8+i
    if i == 0:
        opp1 = 7 
        opp2 = 8
    if i == 1:
        opp1 = 6
        opp2 = 9
    if i == 2:
        opp1 = 5
        opp2 = 10
    if i == 3:
        opp1 = 4 
        opp2 = 11 
    if i == 4:
        opp1 = 3 
        opp2 = 12
    if i == 5:
        opp1 = 2
        opp2 = 13
    if i == 6:
        opp1 = 1
        opp2 = 14
    if i == 7:
        opp1 = 0 
        opp2 = 15

    add_to_hand = 0
    if i >= 0 and i <= 7:
        if opponent_board[opp1] > 0 and opponent_board[opp2] > 0:
            add_to_hand = opponent_board[opp1] + opponent_board[opp2]
            opponent_board[opp1] = 0
            opponent_board[opp2] = 0

    return add_to_hand
    #return opp1, opp2

# Define how a turn works
def turn(current_board, opponent_board, start):
    hand = 0
    
    """ Start by putting all pebbles of a given hole into
    the hand """
    hand += current_board[start]
    current_board[start] = 0
    i = start 
    
    """ To move, put one pebble from hand into the neighbouring
    hole of the current board, until it is empty."""
    while hand > 0:
        while hand > 0:
            i = (i + 1) % 16
            current_board[i] += 1
            hand -= 1
        if current_board[i] > 1:
            hand += current_board[i]
            current_board[i] = 0 
            
            """ Eat the pebbles of the opponent, iff both
             of the two opposing holes are filled. 
            """
            hand += eat(i, opponent_board)
    






