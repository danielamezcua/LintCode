from collections import deque
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        result = []
        dq = deque()
        head_linked_list = ListNode(root.val)
        node_linked_list = head_linked_list
        if root.left:
            dq.append((root.left,1))
        if root.right:
            dq.append((root.right,1))
        last_tree_node_depth = 0
        while dq:
            tree_node, depth = dq.popleft()
            
            #add children to the queue of nodes
            if tree_node.left:
                dq.append((tree_node.left, depth+1))
            if tree_node.right:
                dq.append((tree_node.right, depth+1))
                
            #check if the node belongs to the actual linked list
            if depth != last_tree_node_depth:
                result.append(head_linked_list)
                head_linked_list = ListNode(tree_node.val)
                node_linked_list = head_linked_list
            else:
                node_linked_list.next = ListNode(tree_node.val)
                node_linked_list = node_linked_list.next
            last_tree_node_depth = depth
        result.append(head_linked_list)
        return result
            