'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''



class Solution(object):
    def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # create variables that records the high and the low (index-wise)
        # these variables will change depending on where the guessing number lands
        low = 0
        high = len(nums) - 1

        # create a while loop
        # that goes until low and high become equal
        while high >= low:
            continue




        # if target is not in nums return -1
        return -1

    

    nums = [-1,0,3,5,9,12]
    target = 9
    
    print(search(nums, target))


        