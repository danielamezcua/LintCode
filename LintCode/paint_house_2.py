class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        def get_mins(array):
            min1 = -1
            min2 = -1
            
            for i in range(len(array)):
                if min1 == -1 or array[i] < array[min1]:
                    min1 = i
                    
            for i in range(len(array)):
                if (min2 == -1 or array[i] < array[min2]) and i != min1:
                    min2 = i
            return min1,min2
        
        # write your code here
        if not costs:
            return 0
        if len(costs) == 0:
            return 0
        if len(costs[0]) == 0:
            return 0
        n_houses = len(costs)
        n_colors = len(costs[0])
        
        min1,min2 = get_mins(costs[0])
        for i in range(1,n_houses):
            for j in range(n_colors):
                if j == min1:
                    costs[i][j] = costs[i][j] + costs[i-1][min2]
                else:
                    costs[i][j] = costs[i][j] + costs[i-1][min1]
            min1,min2 = get_mins(costs[i])
        min1,min2 = get_mins(costs[n_houses-1])
        return costs[n_houses-1][min1]
        