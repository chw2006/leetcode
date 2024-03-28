# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Use DFS for this
        # Find the height of the left and right subtrees. 
        # The height from this current node is 1 + max(left, right)
        # The diameter is the left height + the right height. 
        # If we find one that is larger than the max so far, set it.
        self.longest = 0

        def dfs(node):
            if not node:
                return 0
            
            # Get the heights of both children
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            # Find the diameter and set it to max if it's the largest
            diameter = left_height + right_height
            self.longest = max(diameter, self.longest)
            # We want to return the height from this node. 
            return 1 + max(left_height, right_height)
        
        dfs(root)

        return self.longest

# T: O(N)
# S: O(1), unless we count stack frames, which would be O(N)