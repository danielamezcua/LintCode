#https://codeforces.com/problemset/problem/94/B

def main():
	''' if we visualize friends and relations as a graph, 
	any triangle or any missing triangle would represent a WIN
	the only way that this can not happen is if every node has exactly 
	to relations. furthermore, in order for this to happen there has to be
	exactly 5 relations'''

	n = int(input())
	if n != 5:
		print("WIN")
	else:
		relations_per_node = [0,0,0,0,0]
		for i in range(n):
			friend1, friend2 = (int(f) for f in input().split())
			relations_per_node[friend1-1] += 1
			relations_per_node[friend2-1] += 1

		for i in range(5):
			if relations_per_node[i] != 2:
				print("WIN")
				break
		else:
			print("FAIL")



if __name__ == '__main__':
	main()