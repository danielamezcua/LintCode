class Solution:
    """
    @param s: the given string
    @return: all the possible states of the string after one valid move
    """
    def generatePossibleNextMoves(self, s):
        # write your code here
        
        n = len(s)
        if n == 0 or n == 1:
            return []
        s_char = list(s)
        result = []
        for i in range(n-1):
            if s[i] == s[i+1] and s[i] == '+':
                aux = s_char.copy()
                aux[i] = '-'
                aux[i+1] = '-'
                result.append(''.join(aux))
        return result