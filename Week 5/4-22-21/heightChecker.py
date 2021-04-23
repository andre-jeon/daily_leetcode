from collections import defaultdict
'''
A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.

You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

Return the number of indices where heights[i] != expected[i].

 

Example 1:

Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation: 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.
Example 2:

Input: heights = [5,1,2,3,4]
Output: 5
Explanation:
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.
Example 3:

Input: heights = [1,2,3,4,5]
Output: 0
Explanation:
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.
'''
class Solution(object):
    def heightChecker(heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # # create a variable that is the sorted version of heights
        # sorted_heights = sorted(heights)

        # my_dict = defaultdict(list)

        # for k, v in zip(heights, sorted_heights):
        #     my_dict[k].append(v)

        # # zip height and sorted_heights into a hashmap
        # # mapping = dict(zip(heights, sorted_heights))

        # counter = 0

        # # iterate the hashmap and check if key value is equal
        # for i in my_dict:
        #     # if not then add 1 to counter
        #     if i != my_dict[i]:
        #         counter += 1
        #     continue

        # return my_dict

        sorted_arr = sorted(heights)
        diff = 0
        for s in range(len(sorted_arr)):
            if sorted_arr[s] != heights[s]:
                diff +=1
            else: continue
        return diff
    
    heights = [2,1,2,1,1,2,2,1]
    print(heightChecker(heights))
        