#Problem 973: 1-bit 2-bit characters
#We only need to check that the last item of the array is a 0 and that we are not currently reading a two-bit character


class Solution:
    """
    @param bits: a array represented by several bits. 
    @return: whether the last character must be a one-bit character or not
    """
    def isOneBitCharacter(self, bits):
        # Write your code here
        n = len(bits)
        reading_second_char = False
        for i in range(n):
        	if i == n-1:
        		if not reading_second_char and bits[i] == 0:
        			return True
        		else: 
        			return False
        	if reading_second_char:
        		reading_second_char = False
        	elif bits[i] == 1:
        		reading_second_char = True
        	