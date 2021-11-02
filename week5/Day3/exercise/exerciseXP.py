# Exercise 1 : Built-In Functions
# Instructions
# Python has many built-in functions.
# If you feel that you don’t know how to properly implement them take a look at the python documentation online.

# Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.
# # ---------------------------------------------------------------------------
# class Builtin:
#     def __init__(self, num):
#         self.num = num

#     def __abs__(self):
#         '''
#         using the abs built in function will return the absolute value of the variable
#         '''
#         pass

#     def __int__(self):
#         '''
#         using the int built in function will return the integer value of the variable
#         '''
#         pass
#     def __int__(self):
#         '''
#         using the input built in function will return the input value of the variable
#         '''
#         pass

# num = Builtin(5)
# print(abs(num))
# print(int(5))
# print(input(num))
# print(__doc__)

# ----------------------------------------------------
# Exercise 2: Currencies
# Instructions
# Create the code which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    def __str__(self):
        return f'{str(self.amount)} {str(self.currency)}s'
            
    def __repr__(self):
        return str(self.amount) + " " + str(self.currency) + "s"

    def __int__(self):
        return int(self.amount)
    
    def __add__(self, other):
        if self.currency != other.currency:
            return Exception('Currencies cannot be compared.')
    
    def __iadd__ (self, other):
        if type(other) == int:
            self.amount += other
            return Currency(self.currency, self.amount)
        else:
            self.amount += other.amount
            return Currency(self.currency, self.amount)

c1 = Currency("dollar", 5)
c2 = Currency('dollar', 10)
c3 = Currency("shekel", 5)
c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'
print(c1.__str__())

# >>> int(c1)
# 5
print(c1.__int__())

# >>> repr(c1)
# '5 dollars'
print(c1.__repr__())

# >>> c1 + 5
# 10
print(c1.amount + 5)

# >>> c1 + c2
# 15
print(c1.amount + c2.amount )

# >>> c1 
# 5 dollars
print(c1)

# >>> c1 += 5
# >>> c1
# 10 dollars
c1 += 5
print(c1)
# >>> c1 += c2
# >>> c1
# 20 dollars
c1 += c2
print(c1)

# c1 = c1 += c2
# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>
c1 += c2
print(c1 + c3)

