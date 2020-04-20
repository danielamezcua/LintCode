class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        
        def binary_search(start,end,target):
            if end <= start:
                if A[start] == target:
                    return start
                else:
                    return -1
            
            middle = start + (end-start)//2
            if A[middle] == target:
                return middle
            elif A[middle] < target:
                return binary_search(middle+1,end,target)
            else:
                return binary_search(start,middle-1,target)
            
        n = len(A)
        if n == 0:
            return [-1,-1]
            
        start = 0
        end = n - 1
        #find rightmost index
        index_1 = binary_search(start,end,target)
        aux_index = index_1
        while aux_index != -1 and aux_index < n - 1:
            aux_index = binary_search(aux_index+1,end,target)
            if aux_index != -1:
                index_1 = aux_index
        
        if index_1 == - 1:
            return [-1,-1]
            
        #now find the left most index
        index_2 = binary_search(0, index_1 - 1, target)
        aux_index = index_2
        while aux_index != -1 and aux_index > 0:
            aux_index = binary_search(0,aux_index-1,target)
            if aux_index != -1:
                index_2 = aux_index
        
        if index_2 == - 1:
            return [index_1,index_1]
        else:
            return [index_2,index_1]