#https://codeforces.com/problemset/problem/1337/B

def main():
	t = int(input())
	for i in range(t):
		h,n,m = (int(i) for i in input().split())

		while h > 20 and n > 0:
			h = h//2 + 10
			n-=1

		while h > 0 and m > 0:
			h-=10
			m -= 1

		if h <= 0:
			print("YES")
		else:
			print("NO")

if __name__ == "__main__":
	main()