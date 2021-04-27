'''
Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:

Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
Example 2:

Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit. 
'''


class Solution(object):
    def secondHighest(s):
        """
        :type s: str
        :rtype: int
        """
        # we only need numbers
        # we need figure out the way to separate number and char
        
        # brute force approach:

        nums = []

        # iterate string and check if i is a number
        for i in s:
            # if i is a digit(a number) then add it to nums
            if i.isdigit():
                nums.append(int(i))
            continue

        # get rid of duplicates
        # [1, 2, 3]
        nums2 = sorted(list(set(nums)), reverse = True)

        if len(nums2) < 2:
            return -1
        return nums2[1]



        
    s = "abc1111"
    print(secondHighest(s))
