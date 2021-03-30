'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

 

Example 1:

Input: x = 121
Output: true

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:

Input: x = -101
Output: false
'''

class Solution(object):
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        # check if the number is less than 10 return False
        # i don't belive in single digits being a palindrome
        if x < 10:
            return False

        # reverse x and check if it's equal to x
        # checking if stringified x is equal to reversed stringified x
        return str(x) == str(x)[::-1]


    x = 121
    print(isPalindrome(x))

        