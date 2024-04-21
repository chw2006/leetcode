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
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # Find the difference between the root val and the target. abs(target - root.val)
        # Keep track of the min_diff and the min_val. 
        # We can do binary search on this tree, so if the target is smaller than root, look left.
        # If target is larger than root, look right. 
        # If target is equal to root, set that as min_val. 
        min_diff = float("inf")
        min_val = float("inf")

        def dfs(node):
            nonlocal min_diff, min_val
            if not node:
                return
            # Do preorder traversal
            diff = abs(node.val - target)
            # In the case where the diffs are equal, we want the smaller node value
            if diff == min_diff:
                if node.val < min_val:
                    min_val = node.val
            # If diff is smaller than min, update both min and value.
            elif diff < min_diff:
                min_diff = diff
                min_val = node.val
            # Now choose the route based on target value
            if target > node.val:
                dfs(node.right)
            elif target < node.val:
                dfs(node.left)
        
        dfs(root)

        return min_val

# T: O(logN) in the average case. Worst case could be O(N) if tree is not balanced.
# S: O(H)
