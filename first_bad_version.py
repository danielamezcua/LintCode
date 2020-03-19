#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if n == 0:
            return -1
                
        
        #variation of binary search. if we find a true. we look for 
        left = 1
        right = n
        
        
        #if we find false, check if the right one is true. if not, look on the right side
        while left < n:
            if left == right:
                return left
            middle = left + (right-left)//2
            #if we find true, check if the left one is false. if not, look on the left side
            if SVNRepo.isBadVersion(middle):
                if middle > 1 and not SVNRepo.isBadVersion(middle-1):
                    return middle
                else:
                    right = middle
            #if we find false, check if the right one is true. if not, look on the right side
            else:
                if middle < n:
                    if SVNRepo.isBadVersion(middle+1):
                        return middle + 1
                    else:
                        left = middle + 1
                else:
                    #if we reach this point it means the rightmost element is false. so no bad versions are found
                    return -1
        return left
                    
                    
                