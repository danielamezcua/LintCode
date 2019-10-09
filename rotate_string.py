def rotate_string(string,offset):
	string = list(string)
	len_string = len(string)
	offset = offset%len_string
	if offset != 0:
		#Make the first swap
		for i in range(0, offset):
			first = i
			second = offset-i

			aux = string[first]
			string[first] = string[-second]
			string[-second] = aux
		print(string)

		for i in range(0, len_string-offset*2):
			for j in range(offset,0,-1):
				first = j + i
				second = j + i + 1
				aux = string[-first]
				string[-first] = string[-second]
				string[-second] = aux
	return string

def main():
	inp = input().split()
	string = inp[0]
	offset = int(inp[1])
	print(rotate_string(string,offset))

if __name__ == "__main__":
	main()