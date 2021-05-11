'''
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
'''


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        counter = 0
        # iterate arr
        # check if i in arr is odd
            # if it is increase the counter + 1
                # check if counter is 3 
                # if it is return true
            # if it's not counter is 0(reset)
            # and continue 
        
        # return false when it's done
