class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    nuber_of_ways = 0
    def backPackIV(self, nums, target):
        dp_array = [0 for i in range(target+1)]
        for item in nums:
            for i in range(1,target+1):
                if item == i:
                    dp_array[i]+=1
                elif item < i:
                    dp_array[i] = dp_array[i] + dp_array[i-item]
        return dp_array[target]