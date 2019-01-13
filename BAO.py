# -*- coding: utf-8 -*-
"""
Run a game of BAO 10 times and store who won and the turn count.
"""
from BAO_functions import game


for i in range(10):
    p1_board = [2] * 16
    p2_board = [2] * 16 
    hand = 0
    game(p1_board, p2_board)
    # store/append result in a csv file

# To Do:     
#define strategies
