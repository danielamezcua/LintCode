class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here
        
        def count_live_neighbors(i,j):
            #left up, up, right up, right, right down, down, left down, left
            directions = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
            live = 0
            for direction in directions:
                new_i = direction[0] + i
                new_j = direction[1] + j
                if 0 <= new_i < n and 0 <= new_j < m and board[new_i][new_j] == 1:
                    live+=1
            return live
            
        def get_state(i,j,n):
            s = board[i][j]
            if s == 1:
                if n < 2:
                    new_s = 0
                elif n < 4:
                    new_s = 1
                else:
                    new_s = 0
            elif n == 3:
                new_s = 1
            else:
                new_s = 0
            
            return new_s
        
        def end_of_board(i,j):
            if i == n-1 and j == m-1:
                return True
            else:
                return False
        
        def get_new_location(i,j):
            if j == m-1:
                return i+1, 0
            else:
                return i,j+1
        
        def game_of_life_rec(i,j):
            n = count_live_neighbors(i,j)
            s = get_state(i,j,n)
            
            if not end_of_board(i,j):
                new_i, new_j = get_new_location(i,j)
                game_of_life_rec(new_i,new_j)
            
            board[i][j] = s
            
        if board:
            n = len(board)
            m = len(board[0])
            game_of_life_rec(0,0)