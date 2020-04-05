"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        
        if not head or not head.next:
            return head
        
        i = head
        previous = None
        while i:
            aux = i.next
            i.next = previous
            previous = i
            i = aux
        return previous