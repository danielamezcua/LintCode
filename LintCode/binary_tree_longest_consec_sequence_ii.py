"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    
    def dfs(self, node):
        if not node:
            return (None,0,0)
            
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        #check if we can add to downwards increasing sequence
        #if not, we just reset the count.
        #left side
        if left[0] != None and left[0] - 1 == node.val:
            left_increasing = left[1] + 1
        else:
            left_increasing = 1
        
        #right side
        if right[0] != None and right[0] - 1 == node.val:
            right_increasing = right[1] + 1
        else:
            right_increasing = 1
        
        #check if we can add to downards decreasing sequence
        if left[0] != None and left[0] + 1 == node.val:
            left_decreasing = left[2] + 1
        else:
            left_decreasing = 1
        
        if right[0] != None and right[0] + 1 == node.val:
            right_decreasing = right[2] + 1
        else:
            right_decreasing = 1
            
        #how do we get a better sequence? increasing to the left and decreasing to the right?
        #or increasing to the right and decreasing to the left?
        #we substract 1 because in both variables we are taking in count the actual node
        mx = max((left_increasing + right_decreasing - 1), (right_increasing + left_decreasing - 1))
        
        #now we know what is the maximum possible sequence we can get at this node, so we compare it to the result
        self.result = max(mx,self.result)
        
        #the parent node needs to know what is the maximum increasing sequence (USING THIS NODE), 
        #and what is the maximum decreasing sequence (USING THIS NODE)
        max_increasing = max(left_increasing, right_increasing)
        max_decreasing = max(left_decreasing, right_decreasing)
        
        return (node.val, max_increasing, max_decreasing)
        
    def longestConsecutive2(self, root):
        self.result = 0
        n = 2
        if not root:
            return 0
        self.dfs(root)
        return self.result