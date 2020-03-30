def main():
	test_cases = int(input())
	for test_case in range(test_cases):
		m = int(input())
		arr = [int(x) for x in input().split()]
		result = ['0' for i in range(m)]
		found = set()

		#find position of 1
		i = 0
		while arr[i] != 1:
			i+=1

		left = i
		right = i
		result[0] = '1'
		looking = 2

		while left > 0 or right < m-1 or looking <= m:
			#check if we have already seen the number we are looking for
			if looking in found:
				if (right-left+1 == looking):
					result[looking-1] = '1'
				looking+=1
				continue

			#chose between going right or going left
			#go right because left is at leftmost position
			if left == 0:
				right+=1
				if arr[right] == looking and (right-left+1) == looking:
					result[looking-1] = '1'
					looking+=1
				found.add(arr[right])

			#go left because right is at rightmost position
			elif right == (m - 1):
				left-=1
				if arr[left] == looking and (right-left+1) == looking:
					result[looking-1] = '1'
					looking+=1
				found.add(arr[left])
			else:
				if arr[right + 1] < arr[left-1]:
					right+=1
					if arr[right] == looking and (right-left+1) == looking:
						result[looking-1] = '1'
						looking+=1
					found.add(arr[right])
				else:
					left-=1
					if arr[left] == looking and (right-left+1) == looking:
						result[looking-1] = '1'
						looking+=1
					found.add(arr[left])
		print(''.join(result))


if __name__ == "__main__":
	main()