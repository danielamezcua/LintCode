"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param a: the array a
    @return: return the minimal points number
    """
    def getAns(self, a):
        # write your code here
        def take_first(elem):
            return elem.end
        n = len(a)
        a.sort(key=take_first)
        
        #the first interval will be the first reference, for which we need at least 1 point.
        index_ref_interval = 0
        number_points = 1
        for i in range(1,n):
            if a[i].start > a[index_ref_interval].end:
                index_ref_interval = i
                number_points+=1
        return number_points