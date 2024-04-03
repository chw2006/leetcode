# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Base case: Only a single node (start = end), return a list with a single tree node. 
    # Base case: when left and right cross. Return empty array. 
    # Go through every value in the range. 
    # Then recursively call dfs to generate the left subtree. Iterate through the list of trees.
    # Then recursively call dfs to generate the right subtree and iterate through that list of trees.
    # Create the root node, pointing to the leftTree as the left child and rightTree as the right child.
    # Add that to result and return the result. 
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        cache = {}

        def dfs(left, right):
            # Base case: left and right are equal, so create one node and return it
            if left == right:
                return [TreeNode(left)]
            if left > right:
                # This nees to be None because we need to loops below to execute and set the child pointer as None
                return [None]
            # If this value was cached before, return it
            if (left, right) in cache:
                return cache[(left, right)]
            res = []
            # Need right + 1 because we want to include right as a possible value
            for i in range(left, right + 1):
                # Recursively call dfs to get the left and right subtrees
                for leftTree in dfs(left, i - 1):
                    for rightTree in dfs(i + 1, right):
                        # Create the root node with the left and right subtrees as children
                        root = TreeNode(i, leftTree, rightTree)
                        # Add root to result
                        res.append(root)
            # Cache this result so we can re-use
            cache[(left, right)] = res
            return res

        return dfs(1, n)

# T: O(Cn) - Where Cn is the number of distinct BST trees that can be generated with n values. Its actual value is 4^n / n * sqrt(n).
# S: O(Cn) - Space complexity is also O(Cn) since we have to store that many trees. 