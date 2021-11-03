# Instructions :
# Download the_stranger.txt

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message .
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.
# a classmethod that returns a Text instance but with a text file: >>> Text.from_file('the_stranger.txt')

# Create a class called TextModification that inherits from Text.
# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Now, use the provided txt file and try using the class you created above.
# Note: Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)
# import requests module 
# -----------------------------------------------
# import requests 
# def time_search():
#     print('Would you like to see how long it takes to retrieve your request? (yes / no)')
#     user_input = input()
#     if user_input == "yes":
#         # Making a get request 
#         u_input = input("What website would you like to use to check? ")
#         response = requests.get(https://www.nfl.com/) 
#         print(response.elapsed)
#     else:
#         print("ok... next time.")
# time_search()
