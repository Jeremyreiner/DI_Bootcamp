# Write a program that accepts a comma separated sequence of words as input
# and prints the words in a comma-separated sequence after sorting them 
# alphabetically.
# Use List Comprehension
# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world
# --------------------------------------------------------------------------------
user_input = input("Enter words seperated by commas: ")
string_list = user_input.split(",")
string_list.sort()
print(string_list)
ordered_str = ','.join(string_list)
print(ordered_str)

