# Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

# It should do the following:
# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.


# Once your code has decided that the user’s input is valid, it should find out the following:
# All possible anagrams to the user’s word.
# Create an AnagramChecker instance and apply it to the steps created above.
# Display the information about the word in a user-friendly, nicely-formatted message such as:


# YOUR WORD :”MEAT”
# this is a valid English word.
# Anagrams for your word: mate, tame, team.
# --------------------------------------------------------------------------------
from anagram_checker import AnagramChecker
#This file uses anagram_checker.py, anagrams_menu.py, and word.txt

#  If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
def is_user_input_valid(word):
        return len(word.split()) == 1 or word.isalpha()


while True:
    print("YES: Would you like to check to see if a word is an anagram?\nNO: Exit\n ")
    user_choice = input().upper()
    if user_choice in 'NO':
        print("Maybe next time. Goodbye")
        break
    elif user_choice in "YES":
        selected_word = input("Enter a word to retrieve its anagram: ")
        if is_user_input_valid(selected_word):
            clean_word = selected_word.strip()
            f = AnagramChecker()
            anagrams = f.get_annagrams(clean_word)
            msg = f'''Your word: {clean_word} 
            This is a valid word within our library
            Its anagrams are: '''
            print(msg, *anagrams)
        else:
            print("Your word is not a valid word within our library.")



