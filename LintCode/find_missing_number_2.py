from collections import defaultdict
class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, ss):
        #compute how many occurences of each number are there supposed to be
        occ = defaultdict(int)
        for i in range(1,n+1):
            s = str(i)
            for j in s:
                occ[int(j)]+=1
        
        #count the occurences of each number
        occ_s = defaultdict(int)
        for digit in ss:
            occ_s[int(digit)] += 1
        
        #get the digit or digits missing
        missing_digits = []
        for i in range(10):
            if occ[i] != occ_s[i]:
                missing_digits.append(i)
        
        #if it's only one digit, return it
        if len(missing_digits) == 1:
            if (occ[missing_digits[0]] - occ_s[missing_digits[0]]) == 1:
                return missing_digits[0]
            else:
                return missing_digits[0]*10 + missing_digits[0]
            
        #if it's more than one digit, search the missing one between d1d2 and d2d1
        else:
            digit1 = missing_digits[0]
            digit2 = missing_digits[1]

            #if one of the digits it's zero, it can only be the other digit*10, since the numbers
            # are not zero padded
            if digit1 == 0 or digit2 == 0:
                return digit1*10 if digit2 == 0 else digit2*10
            
            n1 = missing_digits[0]*10 + missing_digits[1]
            n2 = missing_digits[1]*10 + missing_digits[0]
            
            
            if n1 > n:
                return n2
            elif n2 > n:
                return n1
            else:
                return n1 if str(n1) not in ss else n2
                
            