#Problem 9. Fizz Buzz.
#https://www.lintcode.com/problem/fizz-buzz/description
#Using only one if

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
    	result = []

    	for i in range(1,n+1):
    		if i%15 == 0:
    			result+= ["fizz buzz"]
    		elif i%5 == 0:
    			result+= ["buzz"]
    		elif i%3 == 0:
    			result+=["fizz"]
    		else:
    			result+= [str(i)]
    	return result

