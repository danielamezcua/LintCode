#https://codeforces.com/problemset/problem/698/A

def main():
	n = int(input())

	dp_arr = [0,0,0]
	days = [int(day) for day in input().split()]
	for day in days:
		gym = dp_arr[0] + 1
		contest = dp_arr[1] + 1

		#gym day
		if day == 2 or day == 3:
			gym = min(dp_arr[1], dp_arr[2])

		#contest
		if day == 1 or day == 3:
			contest = min(dp_arr[0], dp_arr[2])

		#rest
		rest = 1 + min(dp_arr)

		dp_arr = [gym,contest,rest]

	print(min(dp_arr))

if __name__ == "__main__":
	main()