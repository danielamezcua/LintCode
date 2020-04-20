class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        swap_index = 1
        i = 1
        max_element = nums[0]
        while i < n:
            if nums[i] > max_element:
                max_element = nums[i]
                if swap_index != i:
                    #swap and update swap index
                    aux = nums[swap_index]
                    nums[swap_index] = nums[i]
                    nums[i] = aux
                swap_index+=1
            i+=1
        return swap_index