#B. Vasya and Books 
#Codeforces problem number 1073

n = int(input())
stacked_books = [int(element) for element in input().split()]
actual_position_in_sb = 0
positions = [-1]*n
vanya_steps = [int(element) for element in input().split()]

books_to_take_out = 0
actual_position_in_sb = 0


for target_book in vanya_steps:
	#look for target book in the stack of books
	if positions[target_book-1] == -1: #book has not been found yet, so we look for it
		while stacked_books[actual_position_in_sb] != target_book:
			books_to_take_out += 1
			positions[stacked_books[actual_position_in_sb] -1] = actual_position_in_sb
			actual_position_in_sb += 1

		#the book is found
		positions[stacked_books[actual_position_in_sb]-1] = actual_position_in_sb
		books_to_take_out += 1
		actual_position_in_sb += 1
		print(books_to_take_out)
		books_to_take_out = 0
		
	else:
		#book has already been found, so we take 0 books in this step
		print(books_to_take_out)





	