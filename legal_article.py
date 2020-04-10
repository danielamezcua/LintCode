class Solution:
    """
    @param s: the article
    @return: the number of letters that are illegal
    """
    def count(self, s):
        uppercase_allowed = True
        uppercase_required = True
        mistakes = 0
        for character in s:
            if character == '.':
                uppercase_required = True
            elif character == ' ' or character == ',':
                uppercase_allowed = True
            else:
                if uppercase_required:
                    if self.is_lower(character):
                        mistakes+=1
                    uppercase_required = False
                elif self.is_upper(character) and not uppercase_allowed:
                    mistakes+=1
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
        else:
            return False