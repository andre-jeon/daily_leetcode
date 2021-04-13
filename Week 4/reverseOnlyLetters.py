'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''





class Solution(object):
    def reverseOnlyLetters(s):
        """
        :type S: str
        :rtype: str
        """
        # start from the beginning and the end
        # swapping method as if it is reversing the whole thing
        
        # create values start and last
        start = 0
        last = len(s) - 1

        # create a while loop 
        # where while start is less than or equal to last
        while start <= last:
            # the value of start and last switches
            s[start] = s[last], s[last] = s[start]
            # add 1 to start and subtract 1 from last 
            # to get the while loop going
            start += 1
            last -= 1
        
        return s

    s = "ab-cd"
    print(reverseOnlyLetters(s))
        