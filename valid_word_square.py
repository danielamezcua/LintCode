class Solution:
    """
    @param words: a list of string
    @return: a boolean
    """
    def validWordSquare(self, words):
        # Write your code here
        if not words:
            return True
        n_rows = len(words)
        n_cols = len(words[0])
        
        for i in range(n_cols):
            for j in range(n_rows):
                if words[j][i] != words[i][j]:
                    return False
        return True
