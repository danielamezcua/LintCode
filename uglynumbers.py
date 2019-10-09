#LintCode Problem No. 4: Ugly Number II
def get_min(a, nth,i):
	not_found_min = True
	minim = -1

	while not_found_min:
		two = a[2]*i
		three = a[3]*i
		five = a[5]*i
		if two <= three and two <= five:
			minim = two
		elif three <= two and three<=five:
			minim = three
		else:
			minim = five
		if minim == nth:
			#Update the value and get another minimum
			if minim == two:
				a[2] *= 2
			elif minim == three:
				a[3] *= 3
			else:
				a[5] *= 5
		else:
			not_found_min = False
	return minim

def update(a,n,i):
	if a[2]*i == n:
		a[2] *= 2
	elif a[3]*i == n:
		a[3] *= 3
	else:
		a[5] *= 5

def kth_ugly_number(k):
	two = {2: 1, 3:3, 5:5}
	three = {2:2, 3:1, 5:5}
	five = {2:2, 3:3, 5:1}
	nth = 1
	for i in range(1,k):
		min_two = get_min(two, nth,2)
		min_three = get_min(three,nth,3)
		min_five = get_min(five,nth,5)
		print(two,three,five)
		if min_two <= min_three and min_two <= min_five:
			update(two,min_two,2)
			nth = min_two
		elif min_three <= min_three and min_three <= min_five:
			update(three,min_three,3)
			nth = min_three
		else:
			update(five,min_five,5)
			nth = min_five
	return nth

def kth_ugly_number2(k):
	n = 2
	if k == 1:
		return 1
	#While kth number hasn't been printed
	while (k>1):
		division_made = True
		aux_n = n
		#Divide number by 2,3,6,10,15 and 60 until it is equal to 1.
		#If no division is made, it means that the number has other divisor than 2,3 or 5
		while (aux_n != 1 and division_made):
			checker_aux_n = aux_n
			if aux_n%30 == 0:
				aux_n = aux_n/30
			if aux_n%15 == 0:
				aux_n = aux_n/15
			if aux_n%10 == 0:
				aux_n = aux_n/10
			if aux_n%6 == 0:
				aux_n = aux_n/6
			if aux_n%5 == 0:
				aux_n = aux_n/5
			if aux_n%3 == 0:
				aux_n = aux_n/3
			if aux_n%2 == 0:
				aux_n = aux_n/2
			if checker_aux_n == aux_n:
				division_made = False
		if aux_n == 1:
			k-=1
		n+=1
	return n-1

def main():
	k = int(input())
	print(kth_ugly_number(k))

if __name__ == "__main__":
	main()