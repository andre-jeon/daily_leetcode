'''
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
'''
class Solution(object):
    def addStrings(num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # turn both num1 and num2 into integer
        num1, num2 = int(num1), int(num2)
        # add them together and return in string format
        return str(num1 + num2)

    num1 = "11"
    num2 = "123"

    print(addStrings(num1, num2))