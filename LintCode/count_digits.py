def main():
	# Leer el número
	inp = input()
	inp = inp.split()
	n = int(inp[0])
	k = int(inp[1])

	print(count_digits(n,k))

def count_digits(n,k):
	number_in_string = str(n)
	length = len(number_in_string)
	#Empieza así: cada 10 números existe 1 dígito k. Ej: 852 - cada 10 dígitos hay un 2 en las unidades
	divider = 10
	number_of_digits = 1
	number_of_occurrences = 0
	for i in range(0,length):
		digit = int(number_in_string[length-1-i])
		if digit > k:
			#Para evitar que se cuenten los 0s del 0 al 10
			if k != 0 or n >= 100 or divider != 100:
				number_of_occurrences = number_of_occurrences + (int(n/divider) + 1)*10**i
		elif digit == k:
			number_of_occurrences = number_of_occurrences + (int(n/divider))*10**i+1
			#Para evitar que se intente acceder a localidades no válidas
			if i != 0:
				number_of_occurrences = number_of_occurrences + int(number_in_string[length-i:])

		else:
			number_of_occurrences = number_of_occurrences + int(n/divider)*10**i
		divider = divider * 10
	return number_of_occurrences

if __name__ == "__main__":
	main()