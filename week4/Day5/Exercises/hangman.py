word = "secret"
errors = 6
gusses = []
done = False

#use the letters in the word to make the underscore line markers for each letter
while done == False:
    print(gusses)
    for letter in word:
        if letter.lower() in gusses:
            print(letter, end = " ")
        else:
            print("*", end =" ")
    print(" ")
    #collect user input for game
    user_input = input(f"Your you have {errors} attempts left to guess the word. What is your next letter? ").lower()
    gusses.append(user_input)
    # mark errors in guesses that do not match letter in word
    if user_input not in  word.lower():
        errors -= 1
        if errors == 0:
            break
    # for the game to end, you are either out of guesses, or you have guessed the word
    done = True
    for letter in word:
        if letter.lower() not in gusses:
            done = False
# anounce the winner or loser
if done:
    print(f"Congratulations! Youve guessed the word '{word}'")
else:
    print(f"You were not able to correct the right word. The correct word was '{word}'")
