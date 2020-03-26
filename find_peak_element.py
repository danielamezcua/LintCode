class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        #brute force Solution
        n = len(A)
        def find_peak_rec(start,end):
            middle = start +(end-start)//2
            if A[middle-1] < A[middle] > A[middle+1]:
                return middle
            elif A[middle-1] > A[middle]:
                return find_peak_rec(start,middle-1)
            else:
                return find_peak_rec(middle+1,end)
        
        return find_peak_rec(1,n-2)