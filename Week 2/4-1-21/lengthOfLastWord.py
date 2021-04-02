'''
Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
'''



class Solution(object):
    def lengthOfLastWord(s):
        """
        :type s: str
        :rtype: int
        """

        # # check if s only consists of just one letter
        # if s == ' ':
        #     return 0
        
        # if len(s) == 1:
        #     return 1
        
        # if len(s) == 0:
        #     return 0

        # # return the length last word with [-1]
        # return len(s.split()[-1])

        words = s.split()
    
        for word in words[::-1]:
            if word:
                return len(word)
        return 0

    s = "a  a    a     "
    print(lengthOfLastWord(s))