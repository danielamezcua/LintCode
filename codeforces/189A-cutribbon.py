#Codeforces: 189A - Cut Ribbon
#(1 ≤ n, a, b, c ≤ 4000)
#Ex1: 5 5 3 2 - 2
#Ex2: 7 5 5 2 - 2

def main():
	inp = input().split()
	n = int(inp[0])
	a = int(inp[1])
	b = int(inp[2])
	c = int(inp[3])
	#Contains the max number of pieces in max_pieces_array[i] for each ribbon of length i
	max_pieces_array = [0 for i in range(0,n+1)]

	for i in range(1,n+1):
		max_a = 0
		max_b = 0
		max_c = 0

		#Get the maximum value if we make a cut of size a
		if i >= a:
			if i == a:
				max_a = 1
			elif max_pieces_array[i-a] != 0:
				max_a = 1 + max_pieces_array[i-a]

		#Get the maximum value if we make a cut of size b
		if i >= b:
			if i == b:
				max_b = 1
			elif max_pieces_array[i-b] != 0:
				max_b = 1 + max_pieces_array[i-b]

		#Get the maximum value if we make a cut of size c
		if i >= c:
			if i == c:
				max_c = 1
			elif max_pieces_array[i-c] != 0:
				max_c = 1 + max_pieces_array[i-c]

		max_pieces_array[i] = max(max_a,max_b,max_c)

	print(max_pieces_array[n])

if __name__ == "__main__":
	main()
