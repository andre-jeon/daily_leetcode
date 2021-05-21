'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of lowercase and uppercase English letters.

A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.

For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

 

Example 1:

Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:

Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.
'''
# class Solution:
#     def sortSentence(s: str) -> str:

#         # separate where spaces happen
#         # add each words into a list
#         words = s.split()

#         mapping = {}

#         # for loop that list and check the last word, which will be it's index
#         for word in words:

#             # create a dictionary to store the value?
#             if word not in mapping:

#                 # index : word
#                 mapping[int(word[-1])] = word

#         return mapping.values()

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s+ ' '
        word = ''
        arrayOfSentence = []
        for char in s:
            if char == ' ':
                arrayOfSentence.append(word)
                word = ''
            else:
                word = word + char
        dictionary = {}
        for a in arrayOfSentence:
            lastletter = a[len(a)-1]
            dictionary[lastletter] = a[0:len(a)-1]
        temp = []
        for i in sorted(dictionary.keys()):
            temp.append(dictionary[i])
        return ' '.join(temp)



    s = "is2 sentence4 This1 a3"
    print(sortSentence(s))

