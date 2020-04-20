#LintCode problem no 20. Dices Sum
# Throw n dices, the sum of the dices' faces is S. 
#Given n, find the all possible value of S along
# with its probability.
#daniel amezcua sánchez 15/10/2019
import math
class Solution:
	# @param {int} n an integer
	# @return {tuple[]} a list of tuple(sum, probability)
	def dicesSum(self, n):
		#initialize dp matrix
		max_number_of_ways = [[0 for i in range(0,n*6+1)]for i in range(0,n+1)]
		for i in range(1,n+1):
			for j in range(i, i*6+1):
				for k in range(1,7):
					dice = i
					left_to_throw = j - k
					if left_to_throw > 0: #or if it is the first dice
						#now check how many ways are of getting left_to_throw with
						#the rest of the dices
						number_of_ways_rest = max_number_of_ways[i-1][left_to_throw]
						if number_of_ways_rest > 0:
							max_number_of_ways[i][j] = max_number_of_ways[i][j] + number_of_ways_rest
					#when it's the first iteration
					elif i == 1:
						if left_to_throw == 0:
							max_number_of_ways[i][j] = 1
		possible_throws = math.pow(6,n)
		#obtain the possibilites
		result = []
		for i in range(n,n*6+1):
			result.append([i,max_number_of_ways[n][i]/possible_throws])
		return result