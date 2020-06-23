from math import ceil
class Solution:
    """
    @param index: the index to be converted
    @return: return the string after convert.
    """
    def convert(self, index):
        """
        1..702 1
        703..1404 2
        1405..2106 3
        """
        
        i = index // 702 if index%702 == 0 else index//702 + 1
        res = index % 702
        
        if res == 0:
            res = 702
        
        last_letter = res % 26
        if last_letter == 0:
            last_letter = 26
            
        last_letter = chr(64+last_letter)
        
        
        if res > 26:
            res = res - 26
            first_letter = chr(65 + ceil(res/26) - 1)
        else:
            first_letter = ''
            
        return ''.join([str(i), first_letter, last_letter])
        