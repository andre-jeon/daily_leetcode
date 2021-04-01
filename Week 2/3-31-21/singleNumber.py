'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

'''
class Solution(object):
    def singleNumber(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # iterate num in nums
        # add to mapping if it's not already in the mapping
        # give the value 1
        # if the value is in mapping
        # add 1 to the value

        # utilize the count function
        # iterate num in nums
        # if num in nums.count(num) is equal to 1 return num
        # if not continue
        for num in nums:
            if nums.count(num) == 1:
                return num
            else:
                continue


    nums = [4,1,2,1,2]

    print(singleNumber(nums))


        