'''
 --- Directions
Given an array and chunk size, divide the array into many subarrays where each subarray is of length size

 --- Examples
chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
'''

class Solution:
    def chunk(array, size):
        
        final = [array[i * size:(i + 1) * size] for i in range((len(array) + size - 1) // size )]

        return final


    array = [1, 2, 3, 4]
    size = 2

    print(chunk(array, size))