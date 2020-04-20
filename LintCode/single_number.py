#
import math
class Solution:
	"""
	@param A: An integer array
	@return: An integer
	"""
	def singleNumber(self, A):
		# write your code here
		n = len(A)
		bit_vector = 0
		bit_vector_negatives = 0
		for i in range(n):
			if A[i] < 0:
				number_bit = 1 << A[i] * -1
				bit_vector_negatives = bit_vector_negatives ^ number_bit
			else: 
				number_bit = 1 << A[i]
				bit_vector = bit_vector ^ number_bit
		
		if bit_vector == 0:
			return int(math.log2(bit_vector_negatives) * -1)
		else:
			return int(math.log2(bit_vector))
