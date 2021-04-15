'''
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.

 

Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.

Example 2:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".

Example 3:

Input: n = 6
Output: 1
Explanation: 6 in binary is "110".

Example 4:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There aren't any adjacent pairs of 1's in the binary representation of 8, so we return 0.

Example 5:

Input: n = 1
Output: 0
'''

class Solution(object):
    def binaryGap(n):
        """
        :type n: int
        :rtype: int
        """
        # counter that starts with 0
        counter = 1

        # convert n into binary number
        # ['1', '0', '1']
        n = list(bin(n)[2:])

        for i in range(len(n) - 1):
            if n[i] == '1' and n[i + 1] == '0':
                continue
            elif n[i] == '0':
                counter += 1
                

        # for i in n:

        #     # everytime the number is 1 it goes back to 0
        #     if i == '1':
        #         counter = 0
        #     # everything it's zero it gets added 1
        #     elif i == '0':
        #         counter += 1

        # # compare it
        # return counter
        return n



    



    n = 5
    print(binaryGap(n))