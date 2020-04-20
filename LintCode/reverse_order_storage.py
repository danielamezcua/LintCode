"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order 
    """
    def reverseStore(self, head):
        # write your code here
        def reverse_recursive(node):
            if node.next:
                reverse_recursive(node.next)
            array.append(node.val)
            
        array = []
        if head:
            reverse_recursive(head)
        return array