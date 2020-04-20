# Write an algorithm which computes the number of trailing zeros in n factorial.
class Solution:
	def trailingZeros(self,n):
	        count = 0
	        while (n>=5):
	            count+= n//5
	            n = n//5
	        return count