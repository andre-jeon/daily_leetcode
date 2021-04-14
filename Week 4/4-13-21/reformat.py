'''
Given alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.

 

Example 1:

Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:

Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:

Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Example 4:

Input: s = "covid2019"
Output: "c2o0v1i9d"

Example 5:

Input: s = "ab123"
Output: "1a2b3"
'''

class Solution(object):
    def reformat(self, s):
        """
        :type s: str
        :rtype: str
        """
        #we will separate s into two different array, one will be for char, the other for num
        #compare the len of char and int to figure out if this will be possible
        #if possible, proceed, if not, return empty string
        #use loop to add one of char, then int, etc
        char = []
        num = []
        for i in s:
            if i.isalpha():
                char.append(i)
            else:
                num.append(i)
        ans = ""
        # C N C N C char ALWAYS STARTS FIRST IN THIS CASE
        if len(char) == len(num) or abs(len(char) - len(num)) == 1:
            if len(char) > len(num):
                for a in range(len(num)):
                    ans = ans + char[a]
                    ans = ans + num[a]
                ans = ans + char[len(char) - 1]
            elif len(char) < len(num):
                for a in range(len(char)):
                    ans = ans + num[a]
                    ans = ans + char[a]
                ans = ans + num[len(num) - 1]
            else:
                for a in range(len(num)):
                    ans = ans + char[a]
                    ans = ans + num[a]
            return ans
        else:
            return ""