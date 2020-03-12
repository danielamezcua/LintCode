class Solution:
    """
    @param s: the article
    @return: the number of letters that are illegal
    """
    def count(self, s):
        # Write your code here.
        uppercase_allowed = True
        mistakes = 0
        for char in s:
            if char == '.':
                uppercase_allowed = True
            if self.is_upper(char) and not uppercase_allowed:
                mistakes += 1
            elif self.is_lower(char) and uppercase_allowed:
                mistakes += 1
            elif self.is_upper(char):
                uppercase_allowed = False
        return mistakes
    def is_lower(self,char):
        if ord(char) >= 97 and ord(char) <= 122:
            return True
        else:
            return False
    def is_upper(self,char):
        if ord(char) >= 65 and ord(char) <= 90:
            return True
        else
            return False