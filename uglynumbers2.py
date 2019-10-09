def kth_number(k):
	ugly = [0 for i in range(0,k)]
	next_2 = 2
	next_3 = 3
	next_5 = 5

	index_2 = 0
	index_3 = 0
	index_5 = 0
	ugly[0] = 1

	for i in range(1,k):
		min_value = min(next_2,next_3,next_5)
		ugly[i] = min_value
		if min_value == next_2:
			index_2 += 1
			next_2 = ugly[index_2]*2

		if min_value == next_3:
			index_3 += 1
			next_3 = ugly[index_3]*3

		if min_value == next_5:
			index_5 += 1
			next_5 = ugly[index_5]*5

	return ugly[k-1]

def main():
	k = int(input())
	print(kth_number(k))

if __name__ == "__main__":
	main()