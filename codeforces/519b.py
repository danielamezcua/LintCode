#B. A and B and Compilation Errors
#Codeforces problem number 519
#we will obtain the difference between the sum of the errors in the n-step, and the summ of the errors of the n+1 steps
#the result is the number of error that its missing

number_of_errors = int(input())
accumulator = 0

for element in input().split():
	accumulator += int(element)

sum_errors = accumulator
accumulator = 0

for element in input().split():
	accumulator += int(element)

print(sum_errors-accumulator)
sum_errors = accumulator
accumulator = 0

for element in input().split():
	accumulator += int(element)

print(sum_errors-accumulator)