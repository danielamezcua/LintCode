import heapq
from collections import defaultdict
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        nums_freq = defaultdict(int)
        
        #we will use negative values as 
        for num in nums: #n time
            nums_freq[num]-=1
        
        #elements in heap will have the form (number of times, key)
        heap = []
        for item in nums_freq.items(): #n time
            heap.append((item[1], item[0]))
        
        heapq.heapify(heap) #n time
    
        result = []
        for i in range(k): #k times
            result.append(heapq.heappop(heap)[1]) #logn time
        
        #complexity = n + n + n + k*logn = klogn
        return result