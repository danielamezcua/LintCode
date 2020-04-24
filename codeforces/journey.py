#https://codeforces.com/problemset/problem/839/C
from collections import defaultdict

class Graph:
	def __init__(self):
		self.dict = defaultdict(set)

def main():
	n_cities = int(input())
	g = Graph()
	s = []
	visited = set()
	for i in range(0,n_cities-1):
		u, v = (int(j) for j in input().split())
		g.dict[u].add(v)
		g.dict[v].add(u)


	#dfs
	e = 0
	s.append((1,0,1))
	while s:
		city, l, p = s.pop()
		neighbors = [c for c in g.dict[city] if c not in visited]
		n = len(neighbors)
		if n == 0:
			e += l*p
		else:
			new_p = p/n
			for neighbor in neighbors:
				s.append((neighbor, l+1, new_p))
		visited.add(city)

	print(e)


if __name__ == "__main__":
	main()