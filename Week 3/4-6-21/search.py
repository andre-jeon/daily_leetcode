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
        while low <= high:
            # create a variable that checks the middle of the list
            # floor divide will round down numbers to whole numbers
            mid_point = (low + high) // 2

            # check if the index of mid_point of nums
            # is equal to target
            if nums[mid_point] == target:
                return mid_point

            # check if mid_point is less than the target
            if nums[mid_point] < target:
                # it means low can come up mid_point + 1
                # the search starts with the new low
                # starting with mid_point + 1
                low = mid_point + 1
            
            # check if mid_point is greater than the target
            if nums[mid_point] > target:
                # it means high can come down mid_point - 1
                # the search starts with the new high
                # starting with mid_point - 1
                high = mid_point + 1

        # if target is not in nums return -1
        return -1

    

    nums = [-1,0,3,5,9,12]
    target = 9

    print(search(nums, target))


        