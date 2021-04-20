'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Example 4:

Input: x = 0
Output: 0
'''



class Solution(object):
    def reverse(x: int) -> int:
        """
        :type x: int
        :rtype: int
        """


        if x < 0:
            x = str(x)[::-1]
            x = x[0:len(x)-1]
            x = -abs(int(x))
        
        else:
            x = int(str(x)[::-1])

        if -2**31 < x and x < 2**31 - 1:
            return x
        return 0


        # turn x into string
        # '123-'


        # reverse string


        # if it has '-' in the front add negative at the end
        # -abs(n)

        # return it back into int

        # check if -2**31 < ans < 2**31 - 1
        
        # if it qualifies you return ans

        # if not return 0
    x = 0
    print(reverse(x))