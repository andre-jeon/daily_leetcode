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
class Solution:
    def anagram_2(a, b):

        def toDic(str):
            str = str.lower()
            arr = []
            mapping = {}
            for a in str:
                if a.isalpha():
                    arr.append(a)
                continue
            for i in sorted(arr):
                if i not in mapping:
                    mapping[i] = 1
                else:
                    mapping[i] += 1
            return mapping

        if len(toDic(a).keys()) != len(toDic(b).keys()):
            return False
        for k in toDic(a).keys():
            if toDic(a)[k] == toDic(b)[k]:
                continue
            else:
                return False
        return True


    a = 'RAIL! SAFETY!'
    b = 'fairy tales'

    print(anagram_2(a, b))