class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        dp_array = [float('inf') for i in range(amount+1)]
        dp_array[0] = 0
        for coin in coins:
            for i in range(1, amount+1):
                if coin == i:
                    dp_array[i] = 1
                elif coin < i:
                    dp_array[i] = min(dp_array[i], 1 + dp_array[i-coin])
                    
        if dp_array[amount] == float('inf'):
            return -1
        return dp_array[amount]
