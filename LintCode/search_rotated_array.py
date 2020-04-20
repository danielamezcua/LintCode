class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean 
    """
    def search(self, A, target):
        # write your code here

        def search_rotated(start,end,target):
        	#base case
        	if start >= end:
        		if A[start] == target:
        			return start
        		else:
        			return -1

        	middle = start + (end-start)//2

        	if A[middle] == target:
        		return middle
        	#check which part is rotated
        	elif A[end] < A[middle]:
        		#right part is rotated
        		if A[middle] < target or A[start] > target:
        			#target must be on rotated right part
        			return search_rotated(middle+1,end,target)
        		else:
        			#target must be on unrotated left part
        			return search_rotated(start,middle-1,target)
        	elif A[start] > A[middle]:
        		#left part is rotated
        		if target > A[end] or A[middle] > target:
        			#target must be on rotated left side
        			return search_rotated(start,middle-1, target)
        		else:
        			#target must be on unrotated right side
        			return search_rotated(middle+1,end,target)
        	else:
        		#the array is not rotated, so we perform normal binary search
        		if A[middle] > target:
        			return search_rotated(start,middle-1,target)
        		else:
        			return search_rotated(middle+1,end,target)
        n = len(A)
        if n == 0:
        	return -1

        return search_rotated(0,n-1,target)