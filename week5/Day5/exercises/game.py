# Part I - Game.Py
# game.py – this file/module should contain a class called Game. It should have 4 methods:

import random

class Game():
    '''get_user_item(self) – Ask the user to select an item (rock/paper/scissors). 
    Keep asking until the user has selected one of the items – use data validation and looping. 
    Return the item at the end of the function.'''
    def get_user_item(self):
        playing = True
        while playing == True:
            user_input = input("Please enter R: ROCK / P: PAPER / S: SCISSORS: " ).upper()
            if user_input == "R":
                user_input = "rock"
                return user_input
            elif user_input == "P":
                user_input = "paper"
                return user_input
            elif user_input == "S":
                user_input =  "scissors"
                return user_input
            
    def get_computer_item(self):
        '''get_computer_item(self) – Select rock/paper/scissors at random for the computer. 
        Return the item at the end of the function. Use python’s random.choice() function (read about it online).'''

        list = ["rock", "paper", "scissors"]
        return random.choice(list)
        
    def get_game_result(self):
        '''get_game_result(self, user_item, computer_item) – Determine the result of the game.
        Parameters:
        user_item – the user’s chosen item (rock/paper/scissors)
        computer_item – the computer’s chosen (random) item (rock/paper/scissors)
        Return either win, draw, or loss. Where win means that the user has won, 
        draw means the user and the computer got the same item, and loss means that the user has lost.'''

        choices = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

        user_item = Game.get_user_item(Game)
        computer_throw = Game.get_computer_item(Game)

        if choices[user_item] == computer_throw:
            return f"User wins: {user_item}"

        elif choices[computer_throw] == user_item:
            return f"computer wins: {computer_throw}"

        else:
            return"Tie"


# g = Game()
# g.get_game_result()
