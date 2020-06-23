class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        dp_array = [0 for i in range(target+1)]
        dp_array[0] = 1 #there is one way to obtain a 0: the empty array
        
        n = len(nums)
        for i in range(n):
            aux_dp_array = [dp_array[0]]
            for j in range(1, target+1):
                #check if we can put this item in the bag
                if nums[i] <= j:
                    aux_dp_array.append(dp_array[j] + dp_array[j-nums[i]])
                else:
                    aux_dp_array.append(dp_array[j])
            dp_array = aux_dp_array
        return dp_array[target]
