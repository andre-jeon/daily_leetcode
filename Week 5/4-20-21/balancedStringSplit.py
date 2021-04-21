'''
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:

Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:

Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Example 4:

Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", since each substring contains an equal number of 'L' and 'R'
'''

class Solution(object):
    def balancedStringSplit(s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        ans = 0

        # iterate the string
        # "LLLLRRRR"
        for i in s:
            # whatever letter the string starts with you add 1 to counter
            if i == "L":
                counter += 1
            # whatever the letter that is not the first letter subtract 1 from counter
            if i =="R":
                counter -= 1

        # check counter and whenever the counter is equal to 0 add 1 to ans
            if counter == 0:
                ans += 1
        
        return ans
