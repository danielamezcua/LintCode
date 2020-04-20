class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        len_s = len(s)
        len_t = len(t)
        if len_s == len_t:
            first_incongruence = True
            for i in range(len_s):
                if s[i] != t[i]:
                    if not first_incongruence:
                        return False
                    else:
                        first_incongruence = False
            return not first_incongruence
        elif abs(len_s-len_t) == 1:
            if len_s > len_t:   
                s1 = s
                s2 = t
                l = len_s
            else:
                s1 = t
                s2 = s
                l = len_t
            j = 0
            first_incongruence = True
            for i in range(l):
                if j < len(s2) and s1[i] != s2[j]:
                    if not first_incongruence: 
                        return False
                    else:
                        j-=1
                        first_incongruence = False
                j+=1
            return True
        else:
            return False
                
                
                