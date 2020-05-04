"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        #get total of elements in the hash hash table
        elements = []
        size_hash = 0
        for head in hashTable:
            if head:
                #iterate over linked list at this position
                while head:
                    elements.append(head.val)
                    head = head.next
            size_hash+=1
        
        #construct the new hash
        new_size = size_hash*2
        new_hash_table = [None]*new_size
        for element in elements:
            location = element % new_size
            head = new_hash_table[location]
            if head:
                node = head
                while node.next:
                    node = node.next
                node.next = ListNode(element)
            else:
                new_hash_table[location] = ListNode(element)
        return new_hash_table