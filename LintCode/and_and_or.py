class Solution:
    """
    @param n: 
    @param nums: 
    @return: return the sum of maximum OR sum, minimum OR sum, maximum AND sum, minimum AND sum.
    """
    def getSum(self, n, nums):
        #maximum OR sum: just make OR operation between all the numbers
        #minimum OR sum: take the smallest element (or two smallest elements)
        #minimum AND sum: make AND opeartion between all the numbers
        #an AND operation can only yield a smaller or equal number than the smallest of the operators    
        #maximum AND sum: take the biggest element
        if n == 0:
            return 0
            
        min_number = float('inf')
        max_number = float('-inf')
        
        for i in range(n):
            if i == 0:
                max_or = nums[i]
                min_and = nums[i]
            else:
                max_or = max_or | nums[i]
                min_and = min_and & nums[i]
                
            if nums[i] > max_number:
                max_number = nums[i]
            if nums[i] < min_number:
                min_number = nums[i]
        min_or = min_number
        max_and = max_number
        return max_or + min_or + max_and + min_and