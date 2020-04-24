"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    i = 0
    val = -1
    def kthSmallest(self, root, k):
        def find_kth(node):
            if self.val == -1:
                if node.left:
                    find_kth(node.left)
                self.i+=1
                if self.i == k:
                    self.val = node.val
                
                if node.right:
                    find_kth(node.right)
        
        # write your code here
        
        if not root:
            return -1
        find_kth(root)
        return self.val
        