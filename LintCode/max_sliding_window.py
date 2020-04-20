from collections import deque
class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    def maxSlidingWindow(self, nums, k):
        # write your code here
        #find max of the first sliding window
        if len(nums) == 0:
            return []
        if k == 1:
            return nums
        window_maxs = []
        deq = deque()
        len_deq = 0
        #initialize deque
        for i in range(k-1):
            #for the first element
            if not deq:
                deq.append(i)
                len_deq += 1
            else:
                if nums[i] >= nums[deq[0]]:
                    while deq:
                        deq.pop()
                    deq.append(i)
                    len_deq = 1
                else:
                    while nums[i] > nums[deq[len_deq-1]]:
                        deq.pop()
                        len_deq -= 1
                    deq.append(i)
                    len_deq+=1
        
        for i in range(len(nums) - k + 1):
            print(deq)
            j = i + k - 1
            if nums[j] >= nums[deq[0]]:
                    while deq:
                        deq.pop()
                    deq.append(j)
                    len_deq = 1
            else:
                while nums[j] > nums[deq[len_deq-1]]:
                    deq.pop()
                    len_deq -= 1
                deq.append(j)
                len_deq+=1
            window_maxs.append(nums[deq[0]])
            if deq[0] == i:
                deq.popleft()
                len_deq-=1
        return window_maxs