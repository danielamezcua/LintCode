import sys
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)   
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return (pos if pos != hi and a[pos] == x else -1)  # don't walk off the end

def main():
	inp = input().split()
	number_of_programmers = int(inp[0])
	number_of_pairs = int(inp[1])
	number_of_programmers_can_help = [0] * number_of_programmers

	#Inicializar arreglo de programadores
	programmers_hability_unordered = [0] * number_of_programmers

	#Leer la habilidad de cada programador
	hability = input().split()
	for i in range(0,number_of_programmers):
		programmers_hability_unordered[i] = int(hability[i])

	#Ordenar el arreglo de programadores (nlogn)
	programmers_hability_ordered = programmers_hability_unordered.copy()
	programmers_hability_ordered.sort()

	#Guardar en qué posición del arreglo queda cada programador, y el número de programadores a los cuales puede ayudar (nlogn)
	for i in range(0,number_of_programmers):
		position = int((number_of_programmers-1)/2)
		#Búsqueda binaria
		position = binary_search(programmers_hability_ordered, programmers_hability_unordered[i])

		number_of_programmers_can_help[i] = position
		index = 1
		if position != 0:
			while (programmers_hability_ordered[position] == programmers_hability_ordered[position - index]):
				number_of_programmers_can_help[i] -= 1
				index+=1

	number_of_programmers_untouched = number_of_programmers_can_help.copy()
	#Leer las parejas ordenadas
	for i in range(0,number_of_pairs):
		quarrel = input().split()
		p1 = int(quarrel[0]) - 1
		p2 = int(quarrel[1]) - 1
		if number_of_programmers_untouched[p1] > number_of_programmers_untouched[p2]:
			#El primero pierde un programador al que ayudar
			number_of_programmers_can_help[p1] -= 1
		elif number_of_programmers_untouched[p1] < number_of_programmers_untouched[p2]:
			#El segundo pierde un programador al que ayudar
			number_of_programmers_can_help[p2] -= 1
		

	for i in range(0,number_of_programmers):
		sys.stdout.write(str(number_of_programmers_can_help[i]) + " ")

if __name__ == "__main__":
	main()