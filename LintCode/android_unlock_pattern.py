class Solution:
    """
    @param m: an integer
    @param n: an integer
    @return: the total number of unlock patterns of the Android lock screen
    """
    def numberOfPatterns(self, m, n):
        # Write your code here
        def next_valid_steps(pos,used):
            skip = [[0 for j in range(11)] for k in range(11)]
            skip[1][3] = skip[3][1] = 2
            skip[1][7] = skip[7][1] = 4
            skip[3][9] = skip[9][3] = 6
            skip[7][9] = skip[9][7] = 8
            skip[7][3] = skip[3][7] = skip[1][9] = skip[9][1] = skip[4][6] = skip[6][4] = skip[2][8] = skip[8][2] = 5
            
            for i in range(1,10):
                if (i != pos) and (i not in used) and (skip[i][pos] == 0 or skip[i][pos] in used):
                    yield i
                
            
        def dfs(used, actual_pos, n_used):
            if n_used > n:
                return 0
            
            if n_used >= m:
                sum = 1
            else:
                sum = 0
            
            for number in next_valid_steps(actual_pos,used):
                used.add(number)
                sum+= dfs(used,number, n_used+1)
                used.remove(number)
            return sum
        
        
        used = set({1})
        starting_from_corners = dfs(used,1,1)
        
        used = set({5})
        starting_from_center = dfs(used,5,1)
        
        used = set({2})
        starting_from_cross = dfs(used,2,1)
        
        return starting_from_corners*4 + starting_from_center + starting_from_cross*4