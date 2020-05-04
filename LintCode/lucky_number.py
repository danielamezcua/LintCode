class Solution:
	"""
	@param n str: the number n
	@return str: the smallest lucky number  that is not less than n
	"""
	def luckyNumber(self, n):
		def get_number_digits(n):
			number_of_digits = 1
			while n > 10:
				n = n // 10
				number_of_digits+=1
			return number_of_digits

		def find(target, n_5s, n_3s, power, result):
			if n_5s == 0 and n_3s == 0:
				if result > target:
					return result
				else:
					return -1

			if n_3s > 0:
				new_res = result + 3*10**power
				if new_res >= target:
					r = find(target, n_5s, n_3s-1, power-1, result + 3*10**power)
					if r != -1:
						return r

			if n_5s > 0:
				r = find(target, n_5s-1, n_3s, power-1, result + 5*10**power)
				if r != -1:
					return r
			
			return -1

		def get_biggest_number(n_digits):
			power = n_digits-1
			res = 0
			n_5s = n_digits//2
			n_3s = n_digits//2
			while n_5s > 0 or n_3s > 0:
				if n_5s > 0:
					res += 5*10**power
					n_5s-=1
				else:
					res+= 3*10**power
					n_3s -=1
				power-=1

			return res

		def get_smallest_number(n_digits):
			power = n_digits-1
			res = 0
			n_5s = n_digits//2
			n_3s = n_digits//2
			while n_5s > 0 or n_3s > 0:
				if n_3s > 0:
					res += 3*10**power
					n_3s-=1
				else:
					res+= 5*10**power
					n_5s -=1
				power-=1

			return res

		n = int(n)
		number_of_digits = get_number_digits(n)
		if number_of_digits % 2 == 1:
			return str(get_smallest_number(number_of_digits+1))
		else:
			if n > get_biggest_number(number_of_digits):
				return str(get_smallest_number(number_of_digits+2))
			else:
				return str(find(n, number_of_digits/2, number_of_digits/2,number_of_digits-1,0))