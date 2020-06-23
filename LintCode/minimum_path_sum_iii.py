class Solution:
    """
    @param grid: 
    @return: nothing
    """
    def minimumPathSumIII(self, grid):
        def get_directions(i,j):
            #left, up, up left
            directions = [(0,-1),(-1,0),(-1,-1)]
            for direction in directions:
                new_i = i + direction[0]
                new_j = j + direction[1]
                
                if 0 <= new_i < n and 0 <= new_j < m:
                    yield new_i,new_j
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        
        dp_matrix = [[None for j in range(m)] for i in range(n)]
        dp_matrix[0][0] = grid[0][0]
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                possible = [dp_matrix[new_i][new_j] for new_i,new_j in get_directions(i,j)]
                dp_matrix[i][j] = grid[i][j] + min(possible)
        return dp_matrix[n-1][m-1]