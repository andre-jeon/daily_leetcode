'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.
'''


class Solution(object):
    def largestAltitude(gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        # create the value altitude which is 0
        # this value will change as we iterate elements in gain
        altitude = 0

        # we can compare the values to keep the highest point
        highest_point = 0

        # iterate gain and add elements to altitude
        for i in gain:
            altitude += i

            # check if altitude is bigger than highest_point
            if altitude > highest_point:
                # if altitude is higher replace the value of highest_point
                highest_point = altitude

        # when the loop is done return the highest_point
        return highest_point

    
    gain = [-4,-3,-2,-1,4,3,2]
    print(largestAltitude(gain))