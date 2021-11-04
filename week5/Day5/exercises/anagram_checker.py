# What You Will Create
# Anagram Checker
# We will create a program that will ask the user for a word.
# It will check if the word is a valid English word, and then find all possible anagrams for that word.
# Instructions

# get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

# ------------------------------------------

class AnagramChecker:
    def __init__(self, file_name = 'words.txt'):
        with open(file_name) as f:
            self.words = [word.strip().upper() for word in f.readlines()]
            # self.words = list(map(lambda x:x strip(), f.read()))  #lambda also does the same job as the line above
            # for word in self.words:                               #for loop works just like lines 43 and 44
            #     print(word.strip())
    
    def is_valid_word(self, word):      #general rule of methods/ functions that begin with keyword: 'is' function will be boolean (TRUE/ FALSE)
            return word.upper() in self.words

    def get_annagrams(self, word):
        word_sorted = sorted(list(word.upper()))
        anagrams = []
        for other_word in self.words:
            if sorted(list(other_word)) == word_sorted:
                anagrams.append(other_word)
        anagrams.remove(word.upper())
        return anagrams



h = AnagramChecker()
# print(h.is_valid_word('aa'))

print(h.get_annagrams('aa'))