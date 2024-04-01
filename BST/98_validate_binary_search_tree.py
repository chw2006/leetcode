# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # We need to use DFS for this. 
    # The base case is when we reach a null node, we return True
    # Otherwise, we need to make sure that the node is within the bounds we are given.
    # If they are, we call DFS on the left and right subtrees.
    # The left child bounds are left and the value of the root.
    # The right child bounds are the root and right. 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            # Return True if we're at a leaf node.
            if not node:
                return True
            # If node.val is not in bounds, return False
            if not (left < node.val < right):
                return False

            # In order for the tree to be valid, both subtrees must be valid. 
            return (dfs(node.left, left, node.val) and 
                    dfs(node.right, node.val, right))          

        # The initial bounds are -inf and inf
        return dfs(root, float('-inf'), float('inf'))
    
# T: O(N), where N is the number of nodes in the tree.
# S: O(H), where H is the height of the tree, if we are counting stack frames