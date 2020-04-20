#Lint Code Problem 975. 2 keys-keyboard
#The base case is 1 A, for which we do 0 operations. The next base case is 1 A, for which we need 2 operations. 
#To obtain n A's, we have to paste k A's j times. j = n/k. We also need the number of steps we need to obtain k 
#A's. So n = steps[k] + n/k. Note that if, for ex, we have 3 A's and we want to get 6 A's, we don't need to 
#paste 2 times, we just need (n/k) - 1 pastes. But since we need to perform a copy operation before pasting, ((n
#/k) - 1) + 1) = n/k
#There might be several j's (several multiples of n), so we just get the min of these.


class Solution:
    """
    @param n: The number of 'A'
    @return: the minimum number of steps to get n 'A'
    """
    def minSteps(self, n):
        # Write your code here
        steps = [0 for i in range(0,n+1)] #we use one more location to make match location 1 match with 1A, location match 2 with 2As and so on

        #base cases
        if n == 0:
        	return 0

        steps[0] = 0

       	if n == 1:
       		return 2
        	
        steps[1] = 2

        for i in range(2,n):
        	min_steps = i #perform paste operation n times with one A
        	for j in range(2,i/2):
        		if n%j == 0 and (steps[j] + int(n/j)) < min_steps:
        			min_steps = steps[j] + int(n/j)
        	steps[i] = min_steps

        return steps[n-1]