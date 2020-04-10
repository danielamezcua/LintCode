class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        if len(nums) == 0:
            return 0
        sum_dict = {0:-1}
        sum = 0
        max_length = -1
        for i in range(len(nums)):
            sum += nums[i]
            if (sum-k) in sum_dict and i - sum_dict[sum-k] > max_length:
                max_length = i - sum_dict[sum-k]
            if sum not in sum_dict:
                sum_dict[sum] = i
        return max_length