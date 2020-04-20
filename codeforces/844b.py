#B. Rectangles
#Problem number 844: Rectangles

n,m = [int(i) for i in input().split()]

#each element of the row and of the column will contain a pair ('number_of_whites', 'number_of_blacks')
rows = [[0,0] for i in range(n)]
columns = [[0,0] for i in range(m)]
#read row by row
for i in range(n):
	row = [int(element) for element in input().split()]
	for j in range(m):
		if row[j] == 0: #white
			rows[i][0] += 1
			columns[j][0] += 1
		else:
			rows[i][1] += 1 
			columns[j][1] += 1

#count individual sets
number_of_sets = n*m
for count in rows:
	if count[0] > 0:
		number_of_sets += 2**count[0] - 1 - count[0] #total number of subsets - empty subset - individual subsets(counted since the beginning)
	if count[1] > 0:
		number_of_sets += 2**count[1] - 1 - count[1]

for count in columns:
	if count[0] > 0:
		number_of_sets += 2**count[0] - 1 - count[0] #total number of subsets - empty subset - individual subsets(counted since the beginning)
	if count[1] > 0:
		number_of_sets += 2**count[1] - 1 - count[1]

print(number_of_sets)