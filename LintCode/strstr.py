class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        
        #brute force approach. we could improve it by using KMP algorithm to skip comparisons
        n = len(source)
        m = len(target)
        if m == 0:
            return 0
        if m > n:
            return -1
        for i in range(0,n-m+1):
            mismatch = False
            for j in range(m):
                if target[j] != source[i + j]:
                    mismatch = True
                    break
            if not mismatch:
                return i
        return -1