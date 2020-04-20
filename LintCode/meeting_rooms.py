"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    
    def canAttendMeetings(self, intervals):
        #implementation of a quicksort, if the quicksort succeeds, then there 
        #are not any conflicts.
        def compare_meetings(meeting_1, meeting_2):
            #check if meeting 2 is after meeting 1
            if meeting_2.start >= meeting_1.end:
                return 1
            #check if meeting 1 is after meeting 2
            elif meeting_1.start >= meeting_2.end:
                return -1
            return 0
        def quicksort(start,end):
            if start < end:
                index_lowest = start
                pivot_index = end
                for i in range(end-start):
                    comparison = compare_meetings(intervals[start+i],intervals[pivot_index])
                    #conflict
                    if comparison == 0:
                        return False
                    #left is before right
                    if comparison == -1:
                        #swap
                        aux = intervals[start+i]
                        intervals[start+i] = intervals[index_lowest]
                        intervals[index_lowest] = aux
                        index_lowest+=1
                aux = intervals[pivot_index]
                intervals[pivot_index] = intervals[index_lowest]
                intervals[index_lowest] = aux
                return quicksort(start,index_lowest-1) and quicksort(index_lowest+1,end)
            return True
        return quicksort(0,len(intervals)-1)