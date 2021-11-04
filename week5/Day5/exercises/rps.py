# play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). 
# It will do 3 things:

# Get the user’s item (rock/paper/scissors) and remember it
# Get a random item for the computer (rock/paper/scissors) and remember it

# Determine the results of the game by comparing the user’s item and the computer’s item
# Print the output of the game; something like this: “You selected rock. The computer selected paper. 
# You lose”, “You selected scissors. The computer selected scissors. You drew!”

# Return the results of the game as a string: win;draw;loss;, where win means that the user has won, 
# draw means the user and the computer got the same item, and loss means that the user has lost.

from game import Game

def play():
    playing = True
    tally = []
    print("Lets play a game.")
    print("Welcome to tic tac toe")
    print("Would you like to play (yes / no)?")
    play_game = input().lower()
    if play_game == "yes":
        playing = True
        while playing == True:
            game_results = Game.get_game_result(Game)
            
            print(f"The winner is: {game_results}")
            tally.append(game_results)
            print("Would you like to play again (yes / no)? Or Check your game history. (results): ")
            play_game = input().lower()
            if play_game == "yes":
                playing = True
            elif play_game == "results":
                print('; '.join(tally))
                playing = True
            else:
                playing = False
                print("Hope you enjoyed. Have a good day!")
    else:
        print("Hope you enjoyed. Have a good day!")
play()