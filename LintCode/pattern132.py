#Problem 636. 132 pattern 
#i visualize this problem as follows: if you plot a graph with all the points (index,value) in the array,
#you need to find if the line goes up and at some point it goes down, and one point of the right side of the triangle
#is higher than the lowest point of the left side of the triangle
#so we assume there is a triangle and we find the lowest point of the left side. (min array)
#then we test every value from right to left to be the "peak". if it turns out it's not the peak, it's because
#all the values of it's right are higher than it OR they are at the same height of the lowest point of the left
#so the "peak" goes to the right side of the triangle and we keep going to the left, looking for the real peak

class Solution:
	"""
	@param nums: a list of n integers
	@return: true if there is a 132 pattern or false
	"""

	def find132pattern(self, nums):
		# write your code here
		n = len(nums)
		if n == 0:
			return False
		min_values = [0 for i in range(n)]
		min_values[0] = nums[0]
		for i in range(1,n):
			if nums[i] < min_values[i-1]:
				min_values[i] = nums[i]
			else:
				min_values[i] = min_values[i-1]

		stack = []
		for i in range(n-1,0,-1):
			print(stack)
			while (len(stack) > 0 and stack[-1] < nums[i]):
				if stack[-1] > min_values[i-1]:
					return True
				stack.pop()
			stack.append(nums[i])
		return False


