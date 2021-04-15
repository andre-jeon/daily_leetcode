'''
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

 

Example 1:

Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Example 2:

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.

Example 3:

Input: nums = [-1,1,-6,4,5,-6,1,4,1]
Output: [5,-1,4,4,-6,-6,1,1,1]
'''

class Solution(object):
    def frequencySort(nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rev_sorted = sorted(nums,reverse=1)

        # nums.count counts how many of them exists
        return sorted(rev_sorted, key=nums.count)

        # mapping = {}
        # ans = []

        # # iterate nums
        # # and push it into hashmap with the key being it's frequency
        # # mapping = {1: 2, 2: 3, 3: 1}
        # for num in nums:
        #     if num in mapping:
        #         mapping[num] += 1
        #     else:
        #         mapping[num] = 1
        
        # # this line creates a new dictionary sorted by value
        # # sorted_mapping = {3: 1, 1: 2, 2: 3}
        # # Output: [3,1,1,2,2,2]
        # sorted_mapping = dict(sorted(mapping.items(), key=lambda x: x[1]))

        # counter = 0

        # for i in sorted_mapping:

        #     if counter == sorted_mapping[i]:
        #         break
            
        #     counter = sorted_mapping[i]

        #     # 1, 2, 3
        #     freq = sorted_mapping[i]

        #     for j in range(freq):
        #         ans.append(i)
        
        # return ans
    
    # 33221
    # 13322
    nums = [2,3,1,3,2]

    print(frequencySort(nums))



        