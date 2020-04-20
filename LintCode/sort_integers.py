class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    #sorting using selection sort
    def sortIntegers(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return A
        for i in range(n):
            min = i
            for j in range(i,n):
                if A[j] < A[min]:
                    min = j
            aux = A[i]
            A[i] = A[min]
            A[min] = aux
        return A
