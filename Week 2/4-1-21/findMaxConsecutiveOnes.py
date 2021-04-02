'''
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3

Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
'''


class Solution(object):
    def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        ans = []

        # iterate the list
        for num in nums:
            # check if num in nums is 1
            if num == 1:
                # if it is counter += 1
                counter += 1
            # if it is not append counter to an empty and counter becomes 0
            else:
                ans.append(counter)
                counter = 0

        # return maximum number in the list
        return max(ans)

    nums = [1,1,0,1,1,1]
    print(findMaxConsecutiveOnes(nums))