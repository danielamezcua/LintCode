"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param A: 
    @param query: 
    @return: nothing
    """
    def intervalXOR(self, A, query):
        
        result = []
        for q in query:
            i = q.start
            k = q.end
            res = 0
            for j in range(i,i+k):
                res = res ^ A[j]
            result.append(res)
        return result
            
