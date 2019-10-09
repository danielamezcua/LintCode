# Write a function that add two numbers A and B.
# Use bit manipulation

def aplusb(a,b):
	if (b == 0):
		return a
	#Bitwise EXCLUSIVE OR to make the sum in the positions that will not cause changes in other bits.
	sum = a ^ b

	#Bitwise AND and shift to the left to obtain the positions that will cause a change in the next bit (the carry)
	sum_carry = (a & b) << 1

	#Now we need to sum the carry
	return aplusb(sum, sum_carry)