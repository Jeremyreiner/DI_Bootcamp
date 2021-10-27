# Instructions
# Hint: Look at the remote learning “Matrix” videos

# The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column,
# select only the alpha characters and connect them, then he replaces every group of symbols between two alpha characters by a space.

# Using his technique, try to decode this matrix:
# from types import new_class


matrix = [
    ["7", "i", "3"],
    ["t", "s", "i"],
    ["h","%" ,"x"],
    ["i", ";" ,"#"],
    ["s", "m", " "],
    ["$", "a", " "],
    [ "#", "t", "%" ],
    [ "^" , "r", "!"]
]

col_a =[]
col_b =[]
col_c = []
def col1():
    for i in matrix:
        col1 = i[0]
        col_a.append(col1)
    str1 = ''.join(col_a)
    for i in str1:
        if i.isalpha() == True:
            print(i)
        else:
           pass
    print(" ")

def col2():
    for i in matrix:
        col2 = i[1]
        col_b.append(col2)
    str2 = ''.join(col_b)
    for i in str2:
        if i.isalpha() == True:
            print(i)
        elif i.isalpha == False:
            pass
        else:
            print("")


def col3():
    for i in matrix:
        col3 = i[2]
        col_c.append(col3)
    str3 = ''.join(col_c)
    for i in str3:
        if i.isalpha() == True:
            print(i)

col1()
col2()
col3()
print("!")











# str1 = len(matrix)
# print(len)
# for i, value in enumerate(matrix[0]):
#     if value.isalpha() == False:
#         if index < (len +1):






