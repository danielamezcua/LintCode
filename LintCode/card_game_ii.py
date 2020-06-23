class Solution:
    """
    @param cost: costs of all cards
    @param damage: damage of all cards
    @param totalMoney: total of money
    @param totalDamage: the damage you need to inflict
    @return: Determine if you can win the game
    """
    def cardGame(self, cost, damage, totalMoney, totalDamage):
        n = len(damage)
        dp_array = [0 for i in range(totalMoney+1)]
        
        for i in range(0, n):
            aux_dp_array = [0]
            for j in range(1,totalMoney+1):
                #check if i can afford to buy this card
                if j >= cost[i]:
                    aux_dp_array.append(max(dp_array[j], damage[i] + dp_array[j-cost[i]]))
                else:
                    aux_dp_array.append(dp_array[j])
                
                if aux_dp_array[j] >= totalDamage:
                    return True
                
            dp_array = aux_dp_array
        return False