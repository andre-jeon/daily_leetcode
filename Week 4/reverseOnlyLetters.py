'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Example 1:

Input: "ab-cd"
Output: "dc-ba"

Example 2:

Input: "-abC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
'''





class Solution(object):
    def reverseOnlyLetters(S):
        """
        :type S: str
        :rtype: str
        """
        # # start from the beginning and the end
        # # swapping method as if it is reversing the whole thing
        # s = list(s)
        
        # # create values start and last
        # start = 0
        # last = len(s) - 1

        # # create a while loop 
        # # where while start is less than or equal to last
        # while start < last:

        #     # check if both pointers are alphabets
        #     if s[start].isalpha() and s[last].isalpha():

        #         # the value of both start and last switches
        #         s[start], s[last] = s[last], s[start]

        #         # add 1 to start and subtract 1 from last 
        #         # to get the while loop going
        #         start += 1
        #         last -= 1

        #     # check if only start is alphabetical
        #     if s[start].isalpha() and not s[last].isalpha():
        #         last -= 1

        #     # check if only last is alphabetical
        #     if not s[start].isalpha() and s[last].isalpha():
        #         start += 1

        
        # return ''.join(s)

        # stack approach
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

        # reverse pointer approach
        ans = []
        j = len(ans) - 1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j -= 1
                ans.append(S[j])
                j -= 1
            else:
                ans.append(x)
        
        return "".join(ans)

    S = "a-bC-dEf-ghIj"
    print(reverseOnlyLetters(S))
        