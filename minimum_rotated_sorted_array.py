class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    #[4,5,6,0,1,2]    
    #[2,1]
    def findMin(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]
        start = 0
        end = n - 1
        
        while start < end:
            middle = start + (end-start)//2
            
            if (middle > 0 and nums[middle] < nums[middle-1]):
                return nums[middle]
            if (middle < n-1 and nums[middle+1] < nums[middle]):
                return nums[middle + 1]
            
            #check which part is unsorted(rotated)
            if nums[start] > nums[middle]: #left part is unsorted
                end = middle - 1
            elif nums[end] < nums[middle]: #right part is unsorted
                start = middle + 1
            else: #array is sorted, so we just return the first position
                return nums[start]
        return nums[start]
            
