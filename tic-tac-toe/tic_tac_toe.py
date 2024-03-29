#from IPython.display import clear_output                                                   # Useful if code is run in Jupyter notebook
import time
from operator import itemgetter
from modules.func import player_choices, game_decider, game_design, move_valid, sms_sender

if __name__ == '__main__':
    print("Welcome to Tic Tac Toe!")
    player1_name = input("You are Player 1. Enter your name: ")
    player2_name = input("Player 2, enter your name: ")
    choices = player_choices(player1_name, player2_name)

    # Initialize game using number pad
    game_pattern = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    replay = True
    
    # Start accepting moves
    game_decided = False
    move = 1
    time.sleep(5)
    game_design(game_pattern)
    
    while replay and not(game_decided):
        
        # Check if game is drawn or not before proceeding!
        if game_pattern.count('X') + game_pattern.count('O') == 9:
            response = input('Game drawn! No one wins! Want a replay? (y/n): ')
            if response.lower() == 'n':
                print("Thanks for playing! Hope you enjoyed Tic-Tac-Toe!")
                replay = False
            else:
                game_pattern = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                game_design(game_pattern)

        # If not drawn, proceed! Odd moves are for Player1 and even moves are for Player2.
        if move%2 != 0:

            move_id = int(input("{p1}, enter the box number to place your {c1}: ".format(p1 = player1_name, c1 = choices['player1'])))
            
            if not move_valid(game_pattern, move_id):
                continue        
            game_pattern[move_id] = choices['player1']
            game_decided = game_decider(game_pattern)
            game_design(game_pattern)
            if game_decided:
                response = input("Congratulations {p1} for winning the game! Want a replay? (y/n): ".format(p1 = player1_name))
                if response.lower() == 'n':
                    sms_sender(player1_name, player2_name)
                    replay = False
                else:
                    game_pattern = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    game_design(game_pattern)
                    game_decided = False
            move += 1
        else:
            move_id = int(input("{p2}, enter the box number to place your {c2}: ".format(p2 = player2_name, c2 = choices['player2'])))
            
            if not move_valid(game_pattern, move_id):
                continue        
            game_pattern[move_id] = choices['player2']
            game_decided = game_decider(game_pattern)
            game_design(game_pattern)
            if game_decided:
                response = input("Congratulations {p2} for winning the game! Want a replay? (y/n): ".format(p2 = player2_name))
                if response.lower() == 'n':
                    sms_sender(player2_name, player1_name)
                    replay = False
                else:
                    game_pattern = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    game_design(game_pattern)
                    game_decided = False
            move += 1
