class Solution:
    # @paramn n: An integer
    # @return: A list of root

    def generateTrees(self, n):
        def copy_tree(root):
            if not root:
                return None
            new_root = TreeNode(root.val)
            if root.left:
                new_root.left = copy_tree(root.left)
            if root.right:
                new_root.right = copy_tree(root.right)
              
            return new_root
            
        def generate_trees_rec(node,left_nodes,right_nodes):
            if not left_nodes and not right_nodes:
                return [node]
            
            trees = []
            left_trees = []
            right_trees = []
            if left_nodes:
                for ln in left_nodes:
                    child_ln = [el for el in left_nodes if el < ln]
                    child_rn = [el for el in left_nodes if el > ln]
                    new_left_node = TreeNode(ln)
                    left_trees += generate_trees_rec(new_left_node,child_ln,child_rn)
            if right_nodes:
                for rn in right_nodes:
                    child_ln = [el for el in right_nodes if el < rn]
                    child_rn = [el for el in right_nodes if el > rn]
                    new_right_node = TreeNode(rn)
                    right_trees += generate_trees_rec(new_right_node,child_ln,child_rn)
            
            if left_trees and right_trees:
                for lt in left_trees:
                    node.left = lt
                    for rt in right_trees:
                        node.right = rt
                        trees.append(copy_tree(node))
            else:
                if left_trees:
                    for lt in left_trees:
                        node.left = lt
                        trees.append(copy_tree(node))
                else:
                    for rt in right_trees:
                        node.right = rt
                        trees.append(copy_tree(node))
            #not_used.add(node.val)
            return trees
                    
                    
                    
        result = []
        if n == 0:
            return [{}]
            
        for i in range(1,n+1):
            root = TreeNode(i)
            left_nodes = [j for j in range(1, root.val)]
            right_nodes = [j for j in range(root.val+1,n+1)]
            result += generate_trees_rec(root,left_nodes,right_nodes)
        return result