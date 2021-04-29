'''
You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:

Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:

Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.
'''
class Solution(object):
    def sumOfUnique(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0
        mapping = {}

        for num in nums:
            if num not in mapping:
                mapping[num] = 0
            mapping[num] += 1
        
        for i in mapping:
            if mapping[i] == 1: ans += i
        
        return ans

        # hashmap = {}
        # for i in nums:
        #     if i in hashmap.keys():
        #         hashmap[i] += 1
        #     else:
        #         hashmap[i] = 1

        # sum = 0
        # for key, value in hashmap.items():
        #     if value == 1: sum += key
        # return sum

    
    nums = [1,2,3,2]
    print(sumOfUnique(nums))
        