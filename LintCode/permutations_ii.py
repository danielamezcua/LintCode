class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    
    [0,1,0,0,9]
    [0,0,0,1,9]
    """

    def permuteUnique(self, nums):
        def dfs(arr,suffix,number_elements_left):
            if number_elements_left == 0:
                result.append(arr.copy())
            else:
                for i in range(number_elements_left):
                    if i > 0 and suffix[i] == suffix[i-1]:
                        continue
                    arr.append(suffix[i])
                    dfs(arr, suffix[0:i] + suffix[i+1:], number_elements_left-1)
                    arr.pop()
                    
        result = []
        n = len(nums)
        nums.sort()
        suffix = nums.copy()
        dfs([], suffix, n)
        return result
                    