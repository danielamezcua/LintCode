class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code here
        if n == 0:
            return 0
        if k == 1 and n > 2:
            return 0
            
        result = [0 for i in range(n)]
        result[0] = (k,0)
        if n > 1:
            result[1] = (k*k,k)
            for i in range(2,n):
                new_number_of_ways = result[i-1][0]*k - result[i-1][1] 
                excluded = result[i-1][0] - result[i-1][1] 
                print(i)
                result[i] = (new_number_of_ways, excluded)
        
        return result[-1][0]
                