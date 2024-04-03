# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Traverse the tree in a postorder fashion (left, right, root)
    # The base case is if we reach a null node, where we can return 0 sum and 0 nodes
    # Call dfs on the left and right subtrees and get the sum and nodes from them.
    # The total sum is sum of left + right + root.val. 
    # The total nodes is 1 + left + right
    # If the total sum // total nodes is root.val, increment count.
    # Return total sum, total nodes for the parent to use
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0

        def dfs(node):
            # Base case, if node is null, return 0 sum, 0 nodes.
            if not node:
                return (0, 0)
            # Get the left sum and num of nodes from the left subtree
            left_sum, left_nodes = dfs(node.left)
            # Get the right sum and num of nodes from the right subtree
            right_sum, right_nodes = dfs(node.right)
            # The sum is the left and right + the root
            total_sum = left_sum + right_sum + node.val
            # Num nodes is left and right + 1 (for the root)
            total_nodes = 1 + left_nodes + right_nodes
            # If the average is equal to the root's val, increment count
            if (total_sum // total_nodes) == node.val:
                self.count += 1
            # Return the sum and nodes for the parent
            return (total_sum, total_nodes)
        
        dfs(root)
        
        return self.count

# T: O(N) - we go through every node in the tree
# S: O(H) - where H is the height of the tree