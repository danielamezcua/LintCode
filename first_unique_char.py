#Assumption: the only characters are the ones contained on the ASCII table

class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        NUM_CHARS = 255
        # Write your code here
        count_and_first_pos = [[0,0] for i in range(0,255)]
        n = len(str)
        for i in range(n):
            ascii = ord(str[i])
            if (count_and_first_pos[ascii][0] == 0):
                count_and_first_pos[ascii][1] = i
            count_and_first_pos[ascii][0] += 1
        
        first_pos = n+1
        for element in count_and_first_pos:
            if element[0] == 1:
                if element[1] < first_pos:
                    first_pos = element[1]
        
        return str[first_pos]        