# -*- coding: utf-8 -*-
"""
Functions that characterize the board.
"""    
def game_area():
    field = []
    for i in range(16):
        field.append(2)
    return field


def print_field(p1_board, p2_board, hand1=0, hand2=0):
    print('-------------- Player One ---------------------')
    print('-----------------------------------------------')
    for i in range(8, 16):
        print('|', p1_board[i], '|', end = '')
    print('\n', '----------------------------------------------')
    for i in range(1, 9):
        print('|', p1_board[(8-i)], '|', end = '')
    print('\n', '----------------------------------------------')
    print('----------------------------------------------')
    for i in range(0, 8):
        print('|', p2_board[(i)], '|', end = '')
    print('\n', '----------------------------------------------')
    for i in range(15, 7, -1):
        print('|', p2_board[(i)], '|', end = '')
    print('\n', '----------------------------------------------')
    print('-------------- Player Two ---------------------')

