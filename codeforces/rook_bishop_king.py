#https://codeforces.com/problemset/problem/370/A

def main():
	#read input (starting and end coordinates)
	start_row, start_col, end_row, end_col = (int(i) for i in input().split())


	'''rook: the rook can go to every position in at most 2 moves. 
	if the end position is at the same row or column,it only needs 1 move'''
	if start_row == end_row or start_col == end_col:
		moves_rook = 1
	else:
		moves_rook = 2

	'''bishop: the bishop can't get to every position in the board.
	it can only get to those fields that are of the same color of
	the field that he is on. For these positions, he can get at every one
	in at most 2 moves. likewise the rook, if the end position is 
	on the same diagonal he only needs 1 move
	'''
	color_start_p = get_color(start_row, start_col)
	color_end_p = get_color(end_row, end_col)
	if color_start_p == color_end_p:
		# to positions are on the same diagonal if |r1-r2| = |c1-c2|
		if abs(start_row - end_row) == abs(start_col - end_col):
			moves_bishop =  1
		else:
			moves_bishop = 2
	else:
		moves_bishop = 0

	'''king: the king can get to any position on the board.
	the fastest way to get to a position is to move diagonally until you reach
	the desired row or col, and the move straight.
	'''
	if abs(start_row - end_row) < abs(start_col-end_col):
		moves_king = abs(start_col - end_col)
	else:
		moves_king = abs(start_row - end_row)

	print(moves_rook, moves_bishop, moves_king)




def get_color(r,c):
	if r % 2 == 0:
		if c % 2 == 0:
			return 1
		else:
			return -1
	else:
		if c % 2 == 0:
			return -1
		else:
			return 1

if __name__ == "__main__":
	main()