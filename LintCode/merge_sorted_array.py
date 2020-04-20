class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        for i in range(m-1,-1,-1):
            A[i+n] = A[i]
        i = 0
        j = 0
        k = 0
        
        while i < m and j < n:
            if A[n + i] < B[j]:
                A[k] = A[n+i]
                i+=1
            else:
                A[k] = B[j]
                j+=1
            k+=1
        
        while j < n:
            A[k] = B[j]
            j+=1
            k+=1