class Solution:
    def chunk(array, size):
        
        final = [array[i * size:(i + 1) * size] for i in range((len(array) + size - 1) // size )]

        return final


    array = [1, 2, 3, 4]
    size = 2

    print(chunk(array, size))