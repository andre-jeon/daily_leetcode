'''
--- Directions
    Write a function that accepts a string.  The function should
    capitalize the first letter of each word in the string then
    return the capitalized string.

--- Examples
    capitalize('a short sentence') --> 'A Short Sentence'
    capitalize('a lazy fox') --> 'A Lazy Fox'
    capitalize('look, it is working!') --> 'Look, It Is Working!'
'''
class Solution:
    def cap(str):
        # create an empty list that will contain the joined words
        words = []

        # split str where spaces happen
        splited_str = str.split()

        for word in splited_str:
            words.append(word[0].upper() + word[1:])

        return ' '.join(words)

    str = 'look, it is working!'
    print(cap(str))