class Solution(object):
    def checkIfPangram(sentence):
        """
        :type sentence: str
        :rtype: bool
        """

        # mapping = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'p': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

        # for i in sentence:
        #     # check if i exists in mapping as a key
        #     if i in mapping:
        #         mapping[i] += 1
        
        # # iterate mapping and check if every value has at least 1
        # for j in mapping:
        #     if mapping[j] < 1:
        #         return False


        # finnessing method
        # if len(set(sentence))==26:
        #     return True
        # else:
        #     return False

        alph = 'abcdefghijklmnopqrstuvwxyz'
        alph = list(alph)

        sentence = list(set(sentence))
        sentence.sort()
        
        if alph == sentence:
            return True
        return False
    
    sentence = "anmt"
    print(checkIfPangram(sentence))
        