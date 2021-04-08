'''
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:

Input: "Hello"
Output: "hello"

Example 2:

Input: "here"
Output: "here"

Example 3:

Input: "LOVELY"
Output: "lovely"
'''

class Solution(object):
    def toLowerCase(str):
        """
        :type str: str
        :rtype: str
        """
        # built in approah
        # return str.lower()

        # hashmap with zip approach
        upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lower = "abcdefghijklmnopqrstuvwxyz"
        h = dict(zip(upper, lower))

        # h = {A : a, B : b...}
        
        ans = ''

        for x in str:

            # if x is capital letter
            if x in h:
                # then add the lowercase version to ans
                ans += h[x]
            
            # if x is lowercase
            else:
                # then just add x to ans
                ans += x
        
        return ans

        # 1 liner code of above code
        # return ''.join([h[x] if x in h else x for x in str])

    str = "Hello"
    print(toLowerCase(str))

        