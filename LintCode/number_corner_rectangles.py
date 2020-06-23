class Solution:
    """
    @param grid: the grid
    @return: the number of corner rectangles
    """
    
    def countCornerRectangles(self, grid):
        #search for rectangles that have i,j as left upper corner
        def search_rectangles(i,j,k,n,m):
            rectangles = 0
            for loc in ones_per_col[j]:
                if loc > i and grid[loc][k]:
                    rectangles+=1
            return rectangles
        
        # Write your code here
        rectangles = 0
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        
        ones_per_row = [[] for i in range(n)]
        ones_per_col = [[] for i in range(m)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ones_per_row[i].append(j)
                    ones_per_col[j].append(i)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for loc in ones_per_row[i]:
                        if loc > j:
                            rectangles += search_rectangles(i,j,loc,n,m)
        
        return rectangles
