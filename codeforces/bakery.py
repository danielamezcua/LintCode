from collections import defaultdict
class Graph:
	def __init__(self):
		self.dict = defaultdict(lambda: {})


def main():
	g = Graph()
	n,m,k = (int(i) for i in input().split())
	minimum = -1
	if k > 0:
		for i in range(m):
			u,v,k = (int(i) for i in input().split())
			if u not in g.dict[v] or k < g.dict[v][u]:
				g.dict[v][u] = k
				g.dict[u][v] = k

		cities_with_storage = set([int(i) for i in input().split()])
		for city in cities_with_storage:
			for neighbor in g.dict[city].keys():
				cost = g.dict[city][neighbor]
				if neighbor not in cities_with_storage and (minimum == - 1 or cost < minimum):
					minimum = cost
	print(minimum)
			



if __name__ == "__main__":
	main()
