# -*- coding: utf-8 -*-
"""
Decision strategies for the starting hole of each turn.
"""

from numpy import random as rand
from random import random
from BAO_functions import turn
from BAO_functions import pebbles_left
from BAO_functions import game_status


def strategies(strategy, current_board, opponent_board):
    """
    Assign a number to each strategy to put into the command to play 
    a game.
    """
    if strategy == 1:
        return random_start(current_board)
    if strategy == 2:
        return max_pebbles(current_board, opponent_board)
    if strategy == 3:
        return min_pebbles_to_steal(current_board, opponent_board)
    if strategy == 4:
        return maxmin(current_board, opponent_board)

def random_start(current_board):  
    """
    Start at a random non-empty hole.
    """     
    start = rand.randint(low = 0, high = 15)
    
    while current_board[start] == 0:
        start = rand.randint(low = 0, high = 15)
        
    return start


def max_pebbles(current_board, opponent_board):
    """
    Start at the (first) hole that maximises the sum of pebbles left 
    at the end of each turn. If none does, start at the hole that minimizes
    the sum of pebbles the opponent will be able to eat in the next
    move.
    """
    sum_pebbles = pebbles_left(current_board)
    intermediate_sum_pebbles = 0
    
    for i in range(0,16):
        frozen_current_board = current_board.copy()
        frozen_opponent_board = opponent_board.copy()
        turn(frozen_current_board, frozen_opponent_board, i)
        if pebbles_left(frozen_current_board) > sum_pebbles:
            intermediate_sum_pebbles = pebbles_left(frozen_current_board)
            start = i

    if sum_pebbles > intermediate_sum_pebbles:
        start = min_pebbles_to_steal(current_board, opponent_board)
        
    return start


def sum_eatable_pebbles(current_board):
    """ take the sum of all pebbles lying in opposite holes of each other
    where both holes are filled with at least one pebble.
    """
    eatable_pebbles = 0
    
    for i in range(0, 8):
        opp1 = 7-i
        opp2 = 8+i
        if current_board[opp1] > 0 and current_board[opp2] > 0:
            eatable_pebbles += current_board[opp1] + current_board[opp2]
            
    return eatable_pebbles


def min_pebbles_to_steal(current_board, opponent_board):
    """
    Start at the (first) hole that minimizes the sum of pebbles
    the opponent will be able to eat in the next move, 
    i.e. minimize the sum of pebbles lying in opposing holes of each other
    where both are filled.
    """
    intermediate_eatable_pebbles = 64
    
    for i in range(0, 16):
        frozen_current_board = current_board.copy()
        frozen_opponent_board = opponent_board.copy()
        turn(frozen_current_board, frozen_opponent_board, i)
        pebbles_to_eat = sum_eatable_pebbles(frozen_current_board)
        if pebbles_to_eat < intermediate_eatable_pebbles:
            intermediate_eatable_pebbles = pebbles_to_eat
            start = i

    return start


def maxmin(current_board, opponent_board):
    """
    Start at the (first) hole that maximizes the difference between the sum of 
    pebbles on the board and the sum of pebbles the opponent will be able
    to eat in the next move.
    """
    diff = -1
    
    for i in range(0, 16):
        frozen_current_board = current_board.copy()
        frozen_opponent_board = opponent_board.copy()
        turn(frozen_current_board, frozen_opponent_board, i)
        intermediate_diff = pebbles_left(frozen_current_board) 
        - sum_eatable_pebbles(frozen_current_board)
        if intermediate_diff > diff:
            diff = intermediate_diff
            start = i
    
    return start


def alpha_strategy(current_board, opponent_board, AI_data):
    """
    Choose the hole as a starting point that has the highest probability
    to get a positive reward.
    """
    status = game_status(current_board, opponent_board)
    start = -1
    rewards = []
    for i in range(16):
        rewards.append(0)
    
    for field in range(16):
        rewards_of_field = AI_data[field]
        try:
            rewards[field] = 100 + rewards_of_field[status]
        except:
            rewards[field] = 100
    
    sum_of_rewards = sum(rewards)
    
    probabilities = []
    for i in range(16):
        probabilities.append(rewards[i]/sum_of_rewards)
    
    while True:
        rand = random()
        for i in range(16):
            lower_bound = 0
            j = 0
            while j < i:
                lower_bound += probabilities[j]
                j += 1
            if rand >= lower_bound and rand < lower_bound + probabilities[i]:
                start = i
                break
        if current_board[start] != 0:
            break
        
    return start