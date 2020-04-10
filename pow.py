class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        
        def pow_rec(x,y):
            if y == 0:
                return 1
            aux = pow_rec(x,y//2)
            if y % 2 == 0:
                return aux*aux
            else:
                return x * aux * aux
                
        if n >= 0:
            return pow_rec(x,n)
        else:
            return 1/pow_rec(x,n*-1)