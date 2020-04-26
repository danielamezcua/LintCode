class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        '''
            len_res: the number of elements we still need to add to the array
            i: the starting index from which we can add elements
            target: the number we need to achieve
            arr: the actual posible solution
        '''
        
        #dfs can be optimized if the array is sorted.
        def dfs(len_res,i,target,arr):
            if len_res == 0:
                if target == 0:
                    result.append(arr.copy())
            else:
                for j in range(i, n-len_res+1):
                    #this line only applies if the array is sorted
                    if A[j] > target:
                        break
                    arr.append(A[j])
                    dfs(len_res-1, j+1, target-A[j], arr)
                    arr.pop()
                    

        result = []            
        n = len(A)
        if n == 0:
            return []
        A.sort()
        dfs(k,0,target,[])
        return result
        
        