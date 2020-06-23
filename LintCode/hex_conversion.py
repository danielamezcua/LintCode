class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """
    def hexConversion(self, n, k):
        def conversion_rec(n,k):
            if n == 0:
                return []
            l = conversion_rec(n//k,k)
            l.append(get_char(n%k))
            
            return l
    
        def get_char(d):
            if d > 9:
                return chr(65 + (d-10))
            else:
                return str(d)
        
        if n == 0:
            return "0"
        
        return ''.join(conversion_rec(n,k))
