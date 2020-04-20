#Codeforces: A-858. K-rounding
import math

def main():
	inp = input().split()
	n = int(inp[0])
	k = int(inp[1])
	number_of_twos = 0
	number_of_fives = 0
	tens = 0

	#Encontrar el número de 2s 
	aux_n = n
	while (aux_n%2 == 0):
		aux_n /= 2
		number_of_twos+=1

	#Encontrar el número de 5s
	aux_n = n
	while(aux_n%5 == 0):
		aux_n /= 5
		number_of_fives+=1

	while (number_of_fives > 0 and number_of_twos >0):
		tens += 1
		number_of_fives-=1
		number_of_twos-=1

	while(tens<k):
		if number_of_fives > 0:
			number_of_fives-=1
			n*= 2
		elif number_of_twos > 0:
			number_of_twos-=1
			n*=5
		else:
			n*=10
		tens+=1

	print(n)
if __name__ == "__main__":
	main()