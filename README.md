# Bao la Swahili

Bao is an east-african two-player strategic game played on a board with 16 holes for each of the players, 8 holes on the inside, 8 on the outside row.
At the beginning of the game, each hole is filled with two pebbles, so there are 64 pebbles in total on the board.



*HOW TO PLAY*

At each turn, a player empties all pebbles of a hole and moves clockwise, dropping a pebble in each consecutive hole. 
If the last pebble is dropped in an empty hole, the turn is over.

If the last pebble is dropped in a hole where there is a pebble, the turn will go on: 
	
**a)** If that hole is part of the outside row, all peppbles are emptied and dropped one after the next into the following holes. If the last
pebble is dropped in an empty hole, the turn is over. If the last pebble is dropped in a hole where there is a pebble, the turn will go on (see a) to c)).

**b)** If that hole is part of the inside row AND both of the other player's opposite holes are filled with pebbles, the player can empty his own plus the two other holes and drop one after the next into the following holes. If the last pebble is dropped in an empty hole, the turn is over. If the last pebble is dropped in a hole where there is a pebble, the turn will go on as described (see a) to c)).

**c)** If the hole is part of the inside row and only one or none of the other player's opposite holes is filled with
pebbles, the player goes on to drop a pebble in each consecutive hole. If the last pebble is dropped in an empty hole, the turn is over. If the last pebble is dropped in a hole where there is a pebble, the turn will go on (see a) to c)).


*THE FUNCTIONS*

board.py defines the board.

strategies.py defines six different strategies to play the game
*def strategies*
	takes current/opponent board as input and then allows to choose between the strategies.
	
*def random_start*
	picks a random, non-empty starting hole from the current board.
	
*def max_pebbles*
	picks a non-empty starting hole from the current board such as to maximize the sum of pebbles left at the end of each turn. If none 	does, the hole that minimizes the sum of pebbles the opponent will be able to eat in the next move is picked.
	
*def min_pebbles_to_steal*
	Start at the (first) hole that minimizes the sum of pebbles the opponent will be able to eat in the next move, i.e. minimize the sum 		of pebbles lying in opposing holes of each other where both are filled.
	
*def maxmin*
    Start at the (first) hole that maximizes the difference between the sum of pebbles on the board and the sum of pebbles the opponent will 	be able to eat in the next move.
    
*def alpha_strategy*
    Choose the hole as a starting point that has the highest probability to get a positive reward.
    
BAO_functions.py includes the basic functions needed to run a game.

*def eat*
    Assign two opposing holes to each front-row hole of the current board. Eat (=take) the pebbles of the opponent, if, and only if, both of 	the two opposing holes are filled with at least one pebble. 
    
*def turn*
    Start the turn by putting all pebbles of a given hole into the hand. To move, put one pebble from hand into the neighbouring hole of the  	current board, until it is empty. If the last pebble from hand is put into a hole where there is at least one pebble, put all into the 	
    hand and eat the opponent's pebbles, if applicable. Continue moving. If a given player has taken up pebbles into the hand and replaced 
    all on the board more than 20 times, he is not allowed to take up more.
    
*def pebbles_left(board)*
    Check how many pebbles are left on a given board.   
    
*def game_status(current_board, opponent_board)*
    Return the status of the board as a hash. Needed for the Learning algorithm.
    
BAO.py defines and starts the game - either one or multiple ones in a row.

*def play_game(strategy_p1, strategy_p2, max_allowed_turn_count)*
    The players take turns until one player has 5 or less pebbles left on their board. Stop if the game takes too long.
    
*def play_multiple_games(strategy_p1, strategy_p2, max_allowed_turn_count, times)*
     The players take turns for the specified amount of games. The outcomes of all games are saved.
