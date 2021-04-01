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
        # utilize the count function
        # iterate num in nums
        # if num in nums.count(num) is equal to 1 return num
        # if not continue
        for num in nums:
            # apparently the count method takes up too much time
            if nums.count(num) == 1:
                return num
            else:
                continue
        
        # List Operation
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()


    nums = [4,1,2,1,2]

    print(singleNumber(nums))


        