"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRangeAux(self,root,k1,k2,result):
        out_of_range = False
        if root.val < k1:
            #Now we don't have to search in the left subtree
            out_of_range = True
        else:
            #Search in the left subtree if exists
            if root.left != None:
                result = self.searchRangeAux(root.left, k1,k2,result)
                
        if root.val > k2:
            #Now we don't have to search in the right subtree
            out_of_range = True
        else:
            if not out_of_range:
                result += [root.val]
            #Search in the right subtree if exists
            if root.right != None:
                result = self.searchRangeAux(root.right,k1,k2,result)
        return result
        
    def searchRange(self, root, k1, k2):
        if root != None:
            return self.searchRangeAux(root,k1,k2,[])
        else:
            return []
    
    