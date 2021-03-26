'''
Given two binary strings a and b, return their sum as a binary string. 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution(object):
    def addBinary(a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # turn string binary a and b into integers
        a = int(a, 2) # 3
        b = int(b, 2) # 1
        
        # add a and b
        # res = 3 + 1
        res = a + b
        
        # .replace("0b","")
        # convert the sum into binary
        # return the binary in a string format
        return bin(res).replace("0b", "")


    a = "11"
    b = "1"
    c = "1010"
    d = "1011"
    
    print(addBinary(a, b))
    print(addBinary(c, d))