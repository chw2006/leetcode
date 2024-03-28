# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # Perform a DFS on the root node
    # If it is equal to p or q, return that node's value.
    # Go down the left subtree first and see if we can find p or q. 
    # Then go down the right subtree.
    # If we receive values from both subtrees, then return the current node as the LCA. 
    # If we receive values from only 1 of the subtrees, return that value as the LCA.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        else:
            return left or right
    
    # Time complexity: O(N)
    # Space complexity: O(N), since recursive stack frames. O(1) not counting stack frames. 