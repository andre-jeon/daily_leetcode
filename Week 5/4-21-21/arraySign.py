'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).

 

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1

Example 2:

Input: nums = [1,5,0,2,-3]
Output: 0
Explanation: The product of all values in the array is 0, and signFunc(0) = 0

Example 3:

Input: nums = [-1,1,-1,1,-1]
Output: -1
Explanation: The product of all values in the array is -1, and signFunc(-1) = -1
'''


class Solution(object):
    def arraySign(nums):
        # import math
        # """
        # :type nums: List[int]
        # :rtype: int
        # """
        # # multiply all the num in nums
        # nums = math.prod(nums)

        # # for loop approach
        # # if you don't want to import anything
        # x = 1
        # for i in nums:
        #     x *= i

        # # check if product is 0
        # if nums == 0:
        #     # if it is, return 0
        #     return 0

        # # check if product is less than 0
        # if nums < 0:
        #     # return -1
        #     return -1
        # return 1

        # optimized approach?

        # check if 0 is in nums
        # return 0 if it contains 0
        if 0 in nums:
            return 0
		
        # set up a initial counter
        count = 0

        # iterate nums to check if i is less than 0
        # or if it's divisible by 2
        for i in nums:

            # if i is less than 0
            if i < 0:
                # add 1 to the counter
                count += 1
        
        # return 1 if count is divisible by 2
        # else return -1

        # odd negaive numbers means negative overall product
        # while even negative numbers mean positive overal product
        return 1 if count % 2 == 0 else -1

    nums = [-1,1,-1,1,-1]
    print(arraySign(nums))