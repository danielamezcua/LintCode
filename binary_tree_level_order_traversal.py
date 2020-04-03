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
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        results = []
        if not root:
            return []
            
        dq = deque()
        dq.append((root,0))
        level = []
        last_node_depth = 0
        while dq:
            node,depth = dq.popleft()
            if depth != last_node_depth:
                results.append(level)
                level = [node.val]
            else:
                level.append(node.val)

            if node.left:
                dq.append((node.left, depth + 1))
            if node.right:
                dq.append((node.right, depth + 1))
            
            last_node_depth = depth
        results.append(level)
        return results