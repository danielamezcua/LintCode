from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        def invert(node):
            aux = node.left 
            node.left = node.right
            node.right = aux
            
        queue = deque()
        if root:
            queue.append(root)
        
        while queue:
            node = queue.popleft()
            invert(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)