"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        # write your code here
        if not head:
            return 0
        
        n_nodes = 1
        iterator = head
        
        while iterator.next:
            n_nodes += 1
            iterator = iterator.next
        
        return n_nodes
