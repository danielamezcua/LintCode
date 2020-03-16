class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    #we do a binary search. If the element is not found, we check the last element we ended up with.
    #if it's lower than our target, then the target would be right after this element
    #if it's greater, then the target would be right before this element
    def search_aux(self,A,target,start,end):
        if end <= start:
            n = len(A)
            if A[start] == target:
                return start
            elif A[start] > target:
                return start
            else:
                return start + 1
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