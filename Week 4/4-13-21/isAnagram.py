'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
'''


class Solution(object):
    def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # my attempt
        # check if the length of s and t is equal
        if len(s) != len(t):
            # if it is not return False
            return False

        # sort both s and t and check if they are equal
        if sorted(s) == sorted(t):
            return True
        return False

        # hashmap approach
        dictionary = {}
        
        for i in s:
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1

        for i in t:
            if i in dictionary:
                dictionary[i] -= 1
            else:
                return False

        for val in dictionary.values():
            if val != 0:
                return False
        
        return True
    
    s = "rat"
    t = "car"

    print(isAnagram(s, t))

