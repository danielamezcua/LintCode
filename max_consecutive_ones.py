class Solution:
    """
    @param nums: a binary array
    @return:  the maximum number of consecutive 1s
    """
    def findMaxConsecutiveOnes(self, nums):
        # Write your code here
        count_ones = 0
        max_count = float('-inf')
        for num in nums:
            if num == 1:
                count_ones += 1
            else:
                if count_ones > max_count:
                    max_count = count_ones
                count_ones = 0
        if count_ones > max_count:
            max_count = count_ones
        return max_count