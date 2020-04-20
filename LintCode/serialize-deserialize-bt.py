"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections
class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if not root:
            return "{}"
            
        data = []
        nodes = [root]
        while True:
            new_nodes = []
            if not nodes:
                break
            for node in nodes:
                if node == "#":
                    data.append("#")
                else:
                    data.append(node.val)
                    if node.left:
                        new_nodes.append(node.left)
                    else:
                        new_nodes.append("#")
                    if node.right:
                        new_nodes.append(node.right)
                    else:
                        new_nodes.append("#")
            nodes = new_nodes
        serialized = '{' + ','.join(str(value) for value in data) + '}'
        return serialized
    
    """@param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        if len(data) == 2:
            return None
            
        #Remove the brackets
        data = data[1:-1].split(',')
        
        #Reverse the list so we can handle it as a stack
        data = data[::-1]
        
        #Auxiliary deque, where we will save the TreeNodes we will process as parents
        dq = collections.deque([TreeNode(int(data.pop()))])
        head = None
        
        while data:
            left_child = data.pop()
            right_child = data.pop()
            parent = dq.popleft()
            if not head:
                head = parent
            if left_child != "#":
                parent.left = TreeNode(int(left_child))
                dq.append(parent.left)
            if right_child != "#":
                parent.right = TreeNode(int(right_child))
                dq.append(parent.right)
        return head