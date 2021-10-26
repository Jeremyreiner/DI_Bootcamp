user_input = input("Please enter a string that you want encrypted in ceasers cyper: ")

try: 
    shift = int(input("Please enter how many letters you want to shift your cypher: ")) #shifts the value of the letter over x amount of letters
except:
   shift = int(input("Please enter how many letters you want to shift your cypher: "))

alphabet = "abcdefghijklmnopqrstuvwxyz"
cypher_code = ''

new_char = 0 #will change according to shift
for i in user_input:
    if i.lower() in alphabet:
        new_char = alphabet.index(i) + shift #using the index of alphabet we will shift x within the index and save as new variable
        cypher_code += alphabet[new_char % 26] # makes the string circular and will cycle z back to a
    else:
        cypher_code += i
print(cypher_code)


reverse_a = "abcdefghijklmnopqrstuvwxyz"[::-1]
# print(reverse_a)
new_char1 = 0
decyper_code = ""
for e in cypher_code:
    if e.lower() in reverse_a:
        new_char1 = reverse_a.index(e) + shift #using the index of alphabet we will shift x within the index and save as new variable
        decyper_code += reverse_a[new_char1 % 26] # makes the string circular and will cycle z back to a
    else:
        decyper_code += e
print(decyper_code)



