class Solution:
    """
    @param n: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, n):
        def reverse_number(n):
            if n == 0:
                return 0, 0
            power, rev = reverse_rec(n//10)
            return (n%10)*(10**power) + rev
        
        def reverse_rec(n):
            if n == 0:
                return 0, 0
            
            power, rev = reverse_rec(n//10)
            return power+1, (n%10)*(10**power) + rev
            
        MAX_NUMBER = 2**32 - 1
        if n > 0:
            reversed_number = reverse_number(n)
            if reversed_number > MAX_NUMBER:
                return 0
        elif n < 0:
            n = n*-1
            reversed_number = reverse_number(n)
            if reversed_number > MAX_NUMBER:
                return 0
            reversed_number = reversed_number * -1
        else:
            return 0
            
        return reversed_number