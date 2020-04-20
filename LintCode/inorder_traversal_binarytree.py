"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        def in_order_traversal(node):
            if node.left:
                in_order_traversal(node.left)
            in_order_array.append(node.val)
            if node.right:
                in_order_traversal(node.right)
        in_order_array = []
        if root:
            in_order_traversal(root)
        return in_order_array
