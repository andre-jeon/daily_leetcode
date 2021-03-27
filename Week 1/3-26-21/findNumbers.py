class Solution(object):
    def findNumbers(nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        ans = 0

        # iterate nums
        for num in nums:
            # check if the len of num is not even
            # num % 2 == 0
            if len(str(num)) % 2 != 0:
                # if its not even then continue
                continue
            # if it is then add 1 to ans
            ans += 1

        # return the length of ans
        return ans


    nums = [12,345,2,6,7896]
    print(findNumbers(nums))