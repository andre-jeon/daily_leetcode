'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

 

Example 1:

Input: x = 4
Output: 2

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.


'''


class Solution(object):
    def mySqrt(x):
        """
        :type x: int
        :rtype: int
        """
        import math
        
        # find a sqrt of x
        return math.floor((math.sqrt(x)))
        
        # return the rounded down to nearest integer
    
    x = 8
    print(mySqrt(x))