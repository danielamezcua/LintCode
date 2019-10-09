#Lint code: Merge two sworted arrays
def main():
	a = input().split()
	for i in range(0,len(a)):
		a[i] = int(a[i])

	b = input().split()
	for i in range(0,len(b)):
		b[i] = int(b[i])

	c = []
	ia = 0
	ib = 0

	len_a = len(a)
	len_b = len(b)


	while ia < len(a) and ib < len(b):
		if a[ia] < b[ib]:
			c.append(a[ia])
			ia+=1
		else:
			c.append(b[ib])
			ib+=1

	if ia != len(a):
		while ia < len(a):
			c.append(a[ia])
			ia+=1

	if ib != len(b):
		while ib < len(b):
			c.append(b[ib])
			ib+=1
	print(c)

if __name__ == "__main__":
	main()