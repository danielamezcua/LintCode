from collections import defaultdict
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: all the values with the highest frequency in any order
    """
    def findFrequentTreeSum(self, root):
        def find_freq_sum(root):
            nonlocal max_freq
            if not root:
                return 0
            s = root.val + find_freq_sum(root.left) + find_freq_sum(root.right)
            frequencies[s] += 1
            if frequencies[s] > max_freq:
                max_freq = frequencies[s]
            return s

        frequencies = defaultdict(int)
        max_freq = 0
        find_freq_sum(root)
    
        return [key for key,value in frequencies.items() if value == max_freq]