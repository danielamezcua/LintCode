class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code her
        if len(num1) > len(num2):
            n1 = num1
            n2 = num2
        else:
            n1 = num2
            n2 = num1
        
        i = 1
        l = len(n2)
        result = []
        carry = 0
        
        while i <= l:
            digit1 = ord(n1[-i]) - 48
            digit2 = ord(n2[-i]) - 48
            
            r = digit1 + digit2 + carry
            if r >= 10:
                carry = 1
                r = r % 10
            else:
                carry = 0
            result.append(chr(48+r))
            i+=1
        
        l = len(n1)
        while i <= l:
            digit = ord(n1[-i]) -48
            r = digit + carry
            if r >= 10:
                carry = 1
                r= r % 10
            else:
                carry = 0
            result.append(chr(48+r))
            i+=1
        
        if carry == 1:
            result.append('1')
        
        result.reverse()
        return ''.join(result)
                