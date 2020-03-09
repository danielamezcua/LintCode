#problem 15: permutations

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        n = len(nums)
        print(self.permute_rec(nums,n))
    	

    def permute_rec(self,nums,n):
    	if n == 1:
    		return nums
    	else:
    		result = []
    		for i in range(0,n):
    			nums = self.swap(nums, 0, i)
    			for sublist in self.permute_rec(nums[1:],n-1):
    				result.append([nums[0]] + sublist)
    			nums = self.swap(nums,0,i)
    		print(result)
    		return result


    def swap(self,nums,l,r):
    	aux = nums[l]
    	nums[l] = nums[r]
    	nums[r] = aux
    	return nums


