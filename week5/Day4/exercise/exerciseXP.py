# Exercise 1 – Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.
# Hint : The generated sentences do not have to make sense.
# Download this word list
# Save it in your development directory.
# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.
# -----------------------------------------------------------------------------------------------

# import random

# # Create a function called get_words_from_file. This function should read the file’s content and 
# # return the words as a collection. What is the correct data type to store the words?
# def get_words_from_file():
#     words = []
#     with open('words.txt','r') as f:
#         for line in f:
#             words.append(line.rstrip('\n'))
#         f.close()
#         return words

# # Create another function called get_random_sentence which takes a single parameter called length. 
# # The length parameter will be used to determine how many words the sentence should have. The function should:
# # use the words list to get your random words.
# # the amount of words should be the value of the length parameter.
# def get_random_sentence(length):
#     sentence = ''
#     return_words = get_words_from_file()
#     random_words = random.choices(return_words, k = length)
#     for word in random_words:
#         sentence += word + ' '
#     # Take the random words and create a sentence (using a python method), the sentence should be lower case.
#     print(sentence.lower)

# def sent_length():
#     num = int(input("Enter a number value for how long your sentence should be: "))
#     if 2 <= num <= 20:
#         get_random_sentence(num)
#     else:
#         raise Exception("Incorrect value enterred")

# # Create a function called main which will:
# # Print a message explaining what the program does.
# def main():
#     print('this exercise we will create a random sentence generator')
#     print("Would you like to make a random sentence? (yes / no) ")
#     user_input = input()
#     if user_input == 'yes':
#         sent_length()
#     else:
#         print("Have a good day.")
# main()

# --------------------------------------------------------------------------
# Exercise 2: Working With JSON
# Instructions
import json
# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
# ----------------------------------------------------------------------------------------
with open('samplejson.json', 'r') as f:
    company = json.load(f)

# print(company['company']['employee']['payable']['7000'])

for key, values in company.items():
        print(key, values['employee']['payable']['salary']) 

company['company']['empployee']['birthday'] = 24

with open('samplejson.json', 'w') as f:
    company = json.load(f)