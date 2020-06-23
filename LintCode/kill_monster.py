class Solution:
    """
    @param n: 
    @param v: 
    @return: nothing
    """
    def killMonster(self, n, v):
        def can_kill(a,b):
            for i in range(5):
                if a[i] < b[i]:
                    return False
            
            return True
            
        def buff_altman(a,b):
            for i in range(5):
                a[i] += b[i]

        if n == 0:
            return 0
        if not v:
            return 0
        altman = v[0]
        killed = set()
        has_killed = True
        number_killed = 0
        while has_killed:
            has_killed = False
            for i in range(1,n+1):
                if i not in killed:
                    if can_kill(altman,v[i]):
                        buff_altman(altman, v[i])
                        has_killed = True
                        number_killed+=1
                        killed.add(i)
                        
        return number_killed