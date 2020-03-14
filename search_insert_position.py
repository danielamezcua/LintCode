class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def search_aux(self,A,target,start,end):
        if end <= start:
            n = len(A)
            if A[end] == target:
                return end
            elif A[end] > target:
                index = end
                while index >= 0 and A[index] > target:
                    index -= 1
                return index + 1
            else:
                index = end
                while index < n and A[index] < target:
                    index += 1
                return index
        middle = (end + start)//2
        if A[middle] == target:
            return middle
        elif A[middle] < target:
            return self.search_aux(A,target, middle + 1, end)
        else:
            return self.search_aux(A,target,start,middle-1)

    def searchInsert(self, A, target):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        return self.search_aux(A,target,0,n-1)