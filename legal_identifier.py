#Legal Identifier
class Solution:
    """
    @param str: The identifier need to be judged.
    @return: Return if str is a legal identifier.
    """
    def isLegalIdentifier(self, str):
        # Write your code here.
        #check if it has at least one character
        n = len(str)
        if n == 0:
            return False
        #check that first character is not a number
        if self.is_digit(str[0]):
            return False
            
        #iterate over rest of identifier
        for i in range(1,n):
            #check if ASCII value corresponds to digit, uppercase letter
            #lowercase letter or underscore
            if not self.is_digit(str[i]) and not self.is_alphabet(str[i]) and not ord(str[i]) == 95:
                return False
        
        return True
            
    def is_digit(self,char):
        if ord(char) >= 48 and ord(char) <= 57:
            return True
        return False
            
    def is_alphabet(self,char):
        if (ord(char) >= 97 and ord(char) <= 122) or (ord(char) >= 65 and ord(char) <= 90):
            return True
        return False