'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
'''


class Solution(object):
    def sortArrayByParity(A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # evens = []
        # odds = []
        # # iterate the list
        # for i in A:

        #     # check if the element is even
        #     if i % 2 == 0:

        #         # if it is add it to evens
        #         evens.append(i)

        #     # if the element is not even
        #     else:

        #         # add it to a separte odds
        #         odds.append(i)

        # # add both ans and ans2 and return them
        # return evens + odds

        evens = []
        odds = []

        for x in A:
            if x % 2 == 0:
                evens.append(x)

        for x in A:
            if x % 2 == 1:
                odds.append(x)


        return evens + odds

        return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])

    A = [3,1,2,4]
    print(sortArrayByParity(A))