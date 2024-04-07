# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Do a modified BST search function
        # If the root value is between low and high, add it to the running sum and search both children
        # If the high value is smaller than the root value, go left. 
        # If the low value is larger than the root value, go right. 

        # Base case: if we have a null node, return 0
        if not root:
            return 0
        # Go left if the high value is smaller than the root
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        # Go right if the low value is larger than the root
        elif root.val < low:
            return self.rangeSumBST(root.right, low, high)
        # The case where the root value is within the range, so try both children
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
# T: O(N) - In the worst case, this is O(N) because it depends on the range that is given. 
# S: O(N) - Counting recurisve stacks, this is O(N) in the case where the tree is unbalanced. 
