# Instructions
# The computer choose a random word
# and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.
# ---------------------------------------------------------
import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'creditcard', 'rush', 'south']
u_input = input("would you like to play hangman (yes / no)? ")
word = random.choice(wordslist) 
def hang_man():
    #swap the letters out for stars in the hidden word
    errors = 6
    guess_list =[]
    done = False
    while not done:
        print(guess_list)
        for letter in word:
            if letter.lower() in guess_list:
                print(letter, end = " ")
            else:
                print("*", end = " ")
        print("")
        
        user_input = input(f"guesses remaining {errors}, whats your next guess? ")
        # if the user input is not already in guess list upload to guess list.
        if user_input in guess_list:
            print(f"Youve already guessed the letter {user_input}. Guess again. ")
        else:
            guess_list.append(user_input.lower())
        # check to see if user letter is in word and if not mark as error
        if user_input.lower() not in word.lower():
            errors -= 1
            if errors == 0:
                break
            # for the game to be over the letters of the word will all be in the guess list
        done = True
        for letter in word:
            if letter.lower() not in guess_list:
                done = False
        if errors == 5:
            print(
            '''
            ____
            |    |
            |    0
            |    
            |
        ____|_____
            '''
        )
        elif errors == 4:
            print(
            '''
            ____
            |    |
            |    0
            |    |
            |
        ____|_____
            '''
        )
        elif errors == 3:
            print(
            '''
            ____
            |    |
            |    0
            |  < |
            |   / ף
        ____|_____
            '''
        )
        elif errors == 2:
            print(
            '''
            ____
            |    |
            |    0
            |  < ! >
            |   / ף
        ____|_____
            '''
        )
        elif errors == 1:
            print(
            '''
            ____
            |    |
            |    0
            |   <ף>
            |   / !
        ____|_____
            '''
        )
    # alert winners/ losers
    if done:
        print(f"You found the word: {word}")
    else:
        print(f"You ran out of guesses... The word was {word}")


def play():
    if u_input == "yes":
        hang_man()

    else:
        print("Have a good day!")
play()