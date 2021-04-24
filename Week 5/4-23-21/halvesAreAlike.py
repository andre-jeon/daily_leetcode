'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.

Example 3:

Input: s = "MerryChristmas"
Output: false

Example 4:

Input: s = "AbCdEfGh"
Output: true
'''

class Solution(object):
    def halvesAreAlike(s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """

        # divide s into 2 parts with equal length
        # length of s will always be even
        # len(s) // 2 will give us separate strings(2) length

        # slice s with [:len(s) // 2] and [(len(s) // 2) + 1:]
        # 'book'
        # 'bo'
        first = s[:len(s) // 2]
        # 'ok'
        second = s[len(s) // 2:]

        # iterate both strings to see if they have vowels
        vowels = 'aeiouAEIOU'
        f_counter = 0
        s_counter = 0

        for i in first:
            if i in vowels:
                f_counter += 1

        for j in second:
            if j in vowels:
                s_counter += 1

        return f_counter == s_counter
        

            


    
    s = "book"
    print(halvesAreAlike(s))

