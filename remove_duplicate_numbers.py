from collections import deque 
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        #we use a set to keep track of the numbers that already appeared
        #and a queue to keep track of the indexes of the repeated numbers
        queue = deque()
        s = set()
        n = len(nums)
        repeated = 0
        unique = 0
        for i in range(n):
            if nums[i] in s:
                #add to the repeated queue
                repeated+=1
                queue.append(i)
            else:
                unique+=1
                s.add(nums[i])
                #check if there are elements in the queue of repeated
                if repeated > 0:
                    index = queue.popleft()
                    queue.append(i)
                    aux = nums[index]
                    nums[index] = nums[i]
                    nums[i] = aux
        return unique