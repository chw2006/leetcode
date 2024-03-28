# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # We want to do a preorder traversal of the tree.
    # In our DFS we need to keep track of the node and the running total. 
    # Check if the node exists, if not return 0
    # If the node exits, we want to add the node's val to the total
    # We do this by multiplying the total by 10 and adding the val
    # The base case is when we reach a leaf node (both children are None).
    # In this case, return the total.
    # If it's not a leaf node:
    # We then traverse the left and right children of the tree.
    # We can return their sum and pop back up. 
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, total):
            # Base case for a non-existent node
            if not node:
                return 0
            # Get the running total
            total = (total * 10) + node.val 
            # Base case is when we hit a leaf node
            if not node.left and not node.right:
                return total
            # Traverse the left and right child
            return dfs(node.left, total) + dfs(node.right, total)

        return dfs(root, 0)

# T: O(N), we have to traverse every node in the tree
# S: O(N) in the worst case if the tree is skewed. Otherwise, it is O(H), which is the height of the tree. 