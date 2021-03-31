'''
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
'''


class Solution(object):
    def rotateString(A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        # case 1
        # check if the length of A and B is equal
        if len(A) == len(B):
            # check the index of the first letter of A in B
            #
            C = A
            
            for item in range(len(A)):

                C = C + A[item]
                C = C [1:len(C)]

                if C == B:
                    return True

        # if not return False
        return False
    

    A = 'abcde'
    B = 'cdeab'


    print(rotateString(A,B))