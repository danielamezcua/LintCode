from collections import defaultdict
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        # n = len(nums)
        # d = defaultdict(int)
        # for i in range(n):
        #     d[nums[i]] += 1
        
        # for i in range(n):
        #     find = target-nums[i]
        #     if nums[i] == find:
        #         if d[find] > 1:
        #             return [i+1,i+2]
        #     elif d[find] > 0:
        #         #this should be binary search
        #         return [i+1, nums.index(find) + 1]

        #two pointers solution
        n = len(nums)
        i = 0
        j = n - 1

        while i < j:
            r = nums[i] + nums[j]
            if r == target:
                return [i+1, j+1]
            elif r < target:
                i += 1
            else:
                j -= 1