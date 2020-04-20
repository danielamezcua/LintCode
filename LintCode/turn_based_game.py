class Solution:
    """
    @param atk: the atk of monsters
    @return: Output the minimal damage QW will suffer
    """
    def getAns(self, atk):
        # Write your code here
        atk.sort()
        n = len(atk)
        total_pow = 0
        sum = 0
        for i in range(n):
            total_pow += atk[i]
        
        for i in range(n):
            total_pow -= atk[n-1-i]
            sum += total_pow
            
        
        return sum    
