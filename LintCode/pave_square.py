class Solution:
    """
    @param n: The param n means 2*n rectangular square.
    @return: Return the total schemes.
    """
    def getTotalSchemes(self, n):
        dp_array = [0,1,2] + [0 for i in range(n-2)]
        dp_array[1] = 1
        dp_array[2] = 2
        
        for i in range(3,n+1):
            dp_array[i] = dp_array[i-1] + dp_array[i-2]
        
        return dp_array[n]
