'''
--- Directions
    Check to see if two provided strings are anagrams of eachother.
    One string is an anagram of another if it uses the same characters
    in the same quantity. Only consider characters, not spaces
    or punctuation.  Consider capital letters to be the same as lower case

--- Examples
    anagrams('rail safety', 'fairy tales') --> True
    anagrams('RAIL! SAFETY!', 'fairy tales') --> True
    anagrams('Hi there', 'Bye there') --> False
'''

import re

class Solution:
    def anagram_1(stringA, stringB):

        # create a helper function that cleans up the string
        # gets rid of spaces and non alphabet characters in the string
        def cleanup(str):
            return "".join(sorted(re.sub("[^0-9a-zA-Z]+", "", str).lower()))

        # compare both strings to see if they are equal
        return cleanup(stringA) == cleanup(stringB)
    

    stringA = 'Hi there'
    stringB = 'Bye there'

    # print(cleanup(stringA))
    print(anagram_1(stringA, stringB))