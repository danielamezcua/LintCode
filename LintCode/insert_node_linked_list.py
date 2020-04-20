"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):
        # write your code here
        #check if empty linked list
        if not head:
            head = ListNode(val)
            return head
            
        #check if the new node should be the head
        if val <= head.val:
            aux = ListNode(val,next=head)
            head = aux
            return head
        
        #check if insertion is in the middle of the linked ListNode
        it = head
        while it.next:
            if val <= it.next.val:
                aux = ListNode(val,next=it.next)
                it.next = aux
                return head
            it = it.next
        
        #if we reach this point it means we should insert the node at the end
        it.next = ListNode(val)
        return head