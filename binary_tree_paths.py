"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        
        if not root:
            return []
            
        array_of_paths = []
        stack = []
        stack.append((root,[]))
        while stack:
            el = stack.pop()
            node = el[0]
            path = el[1].copy()
            path.append(node.val)
            #check if it's a leaf
            if not node.right and not node.left:
                array_of_paths.append("->".join(str(e) for e in path))
            else:   
                if node.left:
                    stack.append((node.left, path))
                
                if node.right:
                    stack.append((node.right,path))
        return array_of_paths