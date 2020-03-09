#Narcissistic numbers. Brute force approach
import math
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        narc = []
        if n == 1:
            narc.append(0)
        for i in range(10**(n-1), 10**n):
            number = self.get_sum_digits(n,i)
            if number == i:
                narc.append(i)
        return narc
            
        
    def get_sum_digits(self,digits,number):
        sum = 0
        d = 10**(digits-1)
        while number > 0:
            sum += int(math.pow((number // d),digits))
            number = number - d*(number//d)
            d = d//10
        return sum