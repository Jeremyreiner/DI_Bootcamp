# Exercise 1 : Double Dice
# Instructions
import random   # Create a function that will simulate the rolling of a dice. Call it throw_dice. It should return an integer between 1 and 6.
def roll_dice():
    return random.randint(1, 6)

# Create a function called throw_until_doubles.
# It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number, ie. until we reach doubles.
# For example: (1, 2), (3, 1), (5,5) → then stop throwing, because doubles were reached.
# This function should return the number of times it threw the dice in total. In the example above, it should return 3.
def roll_dubbles():
    d1 =roll_dice()
    d2 = roll_dice()
    count =0
    while d1!= d2:
        print(f"Your roll of d1: {d1} and d2: {d2} was not a double")
        count +=1
        d1 =roll_dice()
        d2 = roll_dice()
    return count
print(f"it took {roll_dubbles()} times to roll doubles")


# Create a main function.
# It should throw doubles 100 times (ie. call your throw_until_doubles function 100 times), 
# and store the results of those function calls (in other words, how many throws it took until doubles were thrown, each time) in a collection. 
# (What kind of collection? Read below to understand what we will need the data for, and this should help you decide which data structure to use).
def results_avg(res_list):
    return sum(res_list) / len(res_list)
def main():
    results = []
    for num in range(0, 100):
        results.append(roll_dubbles())
    print(f"It took {sum(results)} tries to return 100 doubles")
    print(f"Your avg amount of throws to reach doubles was {results_avg(results)}")

main()

# After the 100 doubles are thrown, print out a message telling the user how many throws it took in total to reach 100 doubles.
# Also print out a message telling the user the average amount of throws it took to reach doubles. Round this off to 2 decimal places.
# For example:


# If the results of the throws were as follows (your code would do 100 doubles, not just 3):
# (1, 2), (3, 1), (5, 5)
# (3, 3)
# (2, 4), (1, 2), (3, 4), (2, 2)

# Then my output would show something like this:
# Total throws: 8
# Average throws to reach doubles: 2.67.