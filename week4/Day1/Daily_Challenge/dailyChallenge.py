# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.

# Then, print the first and last characters of the given text.

# Construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World
# ---------------------------------------------------------------
user_input = input("Please write a string: ")
string_length = len(user_input)
list = list(user_input)
if len(user_input) > 10:
    print(f"String is too long!! {string_length}")
else: 
    print(f"Your string is too short!! {string_length}")
length = string_length
new_word = ""
print (list)
for i in list:
    new_word += i # in empty word adds a letter for each iteration of the loop
    print(new_word) #each iteration will add another letter to the word
    


