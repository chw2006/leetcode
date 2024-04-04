"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        # Find the difference between the target and the current node. If it is the min, save the node value and its difference. 
        # If the value is smaller than root, search in the left subtree.
        # If it is larger, search in the right subtree
        # At the end of the DFS, return the min_val. 
        self.min_diff = float('inf')
        self.min_val = float('inf')
        
        def dfs(node):
            if not node:
                return None
            # Get the difference between the target and node val
            diff = abs(node.val - target)
            # If it is smaller than min_diff set min_diff and min_val
            if diff < self.min_diff:
                self.min_diff = diff
                self.min_val = node.val

            if target < node.val:
                dfs(node.left)
            elif target > node.val:
                dfs(node.right)
        
        dfs(root)
        
        return self.min_val

# This can also be done iteratively without a stack even. We just keep assigning root to its children. 
# T: O(H) - It depends, but in the worst case it is O(N) while in most cases a binary search tree would provide O(logN), which is the height of the tree. 
# S: O(H) - where H is the height of the tree (if we count stack frames for recursion)