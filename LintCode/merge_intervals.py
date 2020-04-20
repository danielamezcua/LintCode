"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        n = len(intervals)
        if n == 0:
            return []
        intervals.sort(key=lambda x:x.start)
        end_interval = intervals[0].end
        start_interval = intervals[0].start
        result = []
        for i in range(1,n):
            if intervals[i].start > end_interval:
                result.append(Interval(start_interval,end_interval))
                start_interval = intervals[i].start
                end_interval = intervals[i].end
            else:
                end_interval = max(intervals[i].end, end_interval)
        
        result.append(Interval(start_interval,end_interval))
        return result