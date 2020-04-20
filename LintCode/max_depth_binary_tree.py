"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        def max_depth_rec(node,depth):
            if node.left and node.right:
                return max(max_depth_rec(node.left,depth+1), max_depth_rec(node.right,depth+1))
            elif node.left:
                return max_depth_rec(node.left, depth+1)
            elif node.right:
                return max_depth_rec(node.right,depth+1)
            else:
                return depth
        
        if not root:
            return 0
        
        return max_depth_rec(root,1)