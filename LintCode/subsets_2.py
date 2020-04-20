class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        def generate_results(base_array, index):
            results.append(base_array)
            if index < n:
                last_number = None
                for i in range(index, n):
                    new_array = base_array.copy()
                    if last_number != nums[i]:
                        new_array.append(nums[i])
                        generate_results(new_array, i+1)
                    last_number = nums[i]
        # write your code here
        n = len(nums)
        if n == 0:
            return [[]]
        nums.sort()
        results = []
        generate_results([],0)
        return results
