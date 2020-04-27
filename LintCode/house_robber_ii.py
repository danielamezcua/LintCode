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
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber3(self, root):
        #check if it's better to rob the actual house and de "grandchildren" houses
        #or the "children" houses
    
        def house_robbery_rec(node):
            if not node:
                return 0
            if node in visited:
                return visited[node]
    
            sum1 = node.val
            sum2 = 0
            if node.left:
                sum1 += house_robbery_rec(node.left.left)
                sum1 +=  house_robbery_rec(node.left.right)
                sum2 += house_robbery_rec(node.left)
            
            if node.right:
                sum1 += house_robbery_rec(node.right.left)
                sum1 +=house_robbery_rec(node.right.right)
                sum2 += house_robbery_rec(node.right)
            
            mx = max(sum1,sum2)
            visited[node] = mx
            return mx

        if not root:
            return 0
        visited = {}
        return house_robbery_rec(root)
        