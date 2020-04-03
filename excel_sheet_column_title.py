class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        def get_letters(n):
            if n == 0:
                return ""
            
            letter = n%26
            if letter == 0:
                letter = 26
                n-=1
            
            return get_letters(n//26) + chr(64 + letter)
        return get_letters(n)