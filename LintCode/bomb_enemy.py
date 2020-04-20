class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    
    [
        "W",
        "0",
        "0",
        "0",
        "0",
        "0",
        "E",
        "E",
        "E",
        "E",
        "E",
        "E",
        "E",
        "E",
        "0",
        "0"
        ,"0","0","0","0","W",
        "W","W","0","W","W","W","0","0","W","0","W","0","W","E","E","E","E","0","0","0","0",
        "E","W","0","0","W"
        ]
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        e_cols = [-1 for i in range(m)]
        max_killed = 0
        for i in range(n):
            e_row = 0
            #compute number of enemies at this row before wall
            for j in range(m):
                if grid[i][j] == 'E':
                    e_row += 1
                elif grid[i][j] == 'W':
                    break
            
            for j in range(m):
                #compute number of enemies in cols if it hasnt been computed
                if e_cols[j] == -1:
                    e_col = 0
                    for k in range(n):
                        if grid[k][j] == 'E':
                            e_col+=1
                        elif grid[k][j] == 'W':
                            break
                    e_cols[j] = e_col
                
                #compute value if bomb can be put here
                if grid[i][j] == '0' and (e_row + e_cols[j]) > max_killed:
                    max_killed = e_row + e_cols[j]
                #recompute values of enemy on row and column if wall is found
                elif grid[i][j] == 'W':
                    #for row
                    e_row = 0 
                    for k in range(j+1,m):
                        if grid[i][k] == 'E':
                            e_row += 1
                        elif grid[i][k] == 'W':
                            break
                    
                    #for column
                    e_col = 0
                    for k in range(i+1,n):
                        if grid[k][j] == 'E':
                            e_col+=1
                        elif grid[k][j] == 'W':
                            break
                    e_cols[j] = e_col 
        return max_killed