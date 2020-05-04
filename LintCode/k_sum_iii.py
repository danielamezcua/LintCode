class Solution:
    """
    @param a: the array a
    @param k: the integer k
    @param target: the integer target
    @return: return the number of legal schemes
    [1,2,3,4]
    [1,3]
    [2,4]
    """
    def getAns(self, a, k, target):
        # write your code here
        
        def swap(arr,i,j):
            aux = arr[i]
            arr[i] = arr[j]
            arr[j] = aux
        
        def dfs(arr,n,i,k,target):
            if k == 0:
                if target == 0:
                    return 1
                else:
                    return 0
            sum = 0
            for j in range(i,n+1-k):
                sum += dfs(arr,n,j+1,k-1, target - arr[j])
            return sum
            
        odds = []
        even = []
        n = len(a)
        
        if n == 0:
            return 0
            
        if k == 0:
            return 0
            
        for number in a:
            if number % 2 == 0:
                even.append(number)
            else:
                odds.append(number)
        
        n_even = len(even)
        n_odds = len(odds)
        return dfs(even,n_even,0,k,target) + dfs(odds,n_odds,0,k,target)