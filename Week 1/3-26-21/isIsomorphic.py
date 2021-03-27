class Solution(object):
    def isIsomorphic(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # # mapping = {'e' : 1, 'g' : 2}
        # mapping_1 = {}
        # # mapping = {'a' : 1, 'd' : 2}
        # mapping_2 = {}

        # # if the length of s and t is not equal
        # # return false
        # if len(s) != len(t):
        #     return False
        
        # # check the frequency of the char in word
        # # record that into a hashmap
        # for i in s:
        #     if i not in mapping_1:
        #         mapping_1[i] = 0
            
        #     mapping_1[i] += 1

        # for j in t:
        #     if j not in mapping_2:
        #         mapping_2[j] = 0
            
        #     mapping_2[j] += 1

        # counter = 0
        
        # # you go through the first mapping
        # # check if the each value is equal to mapping 2's value 
        # while counter < len(s):
        #     if mapping_1.get(s[counter]) == mapping_2.get(t[counter]):
        #         counter += 1
        #         continue
        #     else:
        #         return False
        
        # return True

        # checking to see if the length of s and t equal 
        if len(set(s)) == len(set(t)):

            # they are equal
            m = {}

    
            for i in range(len(s)):
                # if the letter is not in the hashmap
                if s[i] not in m:
                    # {s[i] : t[i]}
                    # {'e' : 'a'}
                    m[s[i]] = t[i]
                
                # if the letter is in the hashmap
                else:
                    # you want t[i] to equal m[s[i]]
                    # 'a' = 'a' if they are not equal
                    if t[i] != m[s[i]]:
                        return False
            return True
        
        # if the length of s and t is not equal
        # return False
        return False


    
    s = "bbbaaaba"
    t = "aaabbbba"

    print(isIsomorphic(s, t))