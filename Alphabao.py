# -*- coding: utf-8 -*-
"""
Run Bao with a rudimentary learning algorithm for one player.
"""
from BAO_functions import turn
from BAO_functions import pebbles_left
from BAO_functions import game_status
from strategies import strategies
from strategies import alpha_strategy
from board import game_area


def alpha_game(alpha_player, opponent_strategy, AI_data, max_allowed_turn_count):
    """
    Play a game of Bao where one player is the Alpha-Player and each turn
    the hashed game status plus the starting hole is saved in a dictionary.
    """
    p1_board = game_area()
    p2_board = game_area()
    
    turn_count = 0
    dict_of_hashs = {}
    game_states = []
    while pebbles_left(p1_board) > 5 and pebbles_left(p2_board) > 5 and turn_count < 100:
        turn_count += 1
        if alpha_player == 1:
            status = game_status(p1_board, p2_board)
            start = alpha_strategy(p1_board, p2_board, AI_data)
            turn(p1_board, p2_board, start)
            dict_of_hashs.update({status: start})
            game_states.append(status)
            turn(p2_board, p1_board, strategies(opponent_strategy, p2_board, p1_board))
        else:
            turn(p1_board, p2_board, strategies(opponent_strategy, p1_board, p2_board))
            status = game_status(p1_board, p2_board)
            start = alpha_strategy(p2_board, p1_board, AI_data)
            turn(p2_board, p1_board, start)
            dict_of_hashs.update({status: start})
            game_states.append(status)
            
    if turn_count < max_allowed_turn_count:
        if pebbles_left(p1_board) > 5:
            winning_player = 1
            
        if pebbles_left(p2_board) > 5:
            winning_player = 2
    else:
        winning_player = 0
    
    print("Player {} won after {} turns.".format(winning_player, turn_count))
    
    return winning_player, turn_count, dict_of_hashs, game_states


def alpha_bao(alpha_player, opponent_strategy, max_allowed_turn_count, times, text_output):
    """
    Create (and update) a list of dictionaries with the hashed game states and 
    reward for each of the 16 holes.
    Depending on the outcome, the Alpha-Player gets a positive, negative, 
    or no reward after each game.
    Print the wins and average turns for each player.
    """
    AI_data = []
    winners = []
    overall_turns_alpha = 0
    overall_turns_opponent = 0
    avg_turns_alpha = 0
    avg_turns_opponent = 0
    reward = 0
    
    for i in range(0, 16):
        AI_data.append({})
    
    for i in range(times):
        winning_player, turn_count, dict_of_hashs, game_states = alpha_game(alpha_player, opponent_strategy, AI_data, max_allowed_turn_count)
        if winning_player == alpha_player:
            reward = 1
            overall_turns_alpha += turn_count
        if winning_player == 0:
            reward = 0
        else:
            reward = -1
            overall_turns_opponent += turn_count 
            
        for status in game_states:
            reward_of_field = AI_data[dict_of_hashs[status]]
            try:
                reward_of_field.update({status: reward_of_field[status]+ reward})
            except KeyError:
                reward_of_field.update({status: reward})
        
        winners.append(winning_player)

        
    wins_alpha = 0
    wins_opponent = 0
    avg_turns_alpha = 0
    avg_turns_opponent = 0
    
    for i in range(times):
        if alpha_player == 1:
            if winners[i] == 1:
                wins_alpha += 1
            else:
                if winners[i] == 2:
                    wins_opponent += 1
        else:
            if winners[i] == 1:
                wins_opponent += 1
            if winners[i] == 2:
                wins_alpha += 1
    
    ties = times - wins_alpha - wins_opponent
    
    avg_turns_alpha = overall_turns_alpha/wins_alpha
    avg_turns_opponent = overall_turns_opponent/wins_alpha
        
    if alpha_player == 1:
        text = ("Alpha-Player won {} times after an average of {} turns. \nPlayer 2 won {} times after an average of {} turns. \nPlayers tied {} times after {} turns.".format(wins_alpha, avg_turns_alpha, wins_opponent, avg_turns_opponent, ties, max_allowed_turn_count))
    else:
        text = ("Alpha-Player won {} times after an average of {} turns. \nPlayer 2 won {} times after an average of {} turns. \nPlayers tied {} times after {} turns.".format(wins_opponent, avg_turns_opponent, wins_alpha, avg_turns_alpha, ties, max_allowed_turn_count))
    if text_output != 0:
        print(text)
        
    return reward_of_field
        
def run_alpha_game():
    """
    Run Bao with an Alpha-Player multiple times.
    """
    alpha_player = 1
    opponent_strategy = 1 
    max_allowed_turn_count = 100
    print_data = 1
    times = 100
    reward_of_field = alpha_bao(alpha_player, opponent_strategy, max_allowed_turn_count, times, print_data)
    
run_alpha_game()




