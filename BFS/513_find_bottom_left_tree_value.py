# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # The left-most bottom value in the tree can actually be towards the right, but on the last level of the tree. 
    # So we need to use BFS.
    # Add values from right to left so that we guarantee node points to left at the end of traversal.
    # Return node.val
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque()
        # Keep node in-scope when we return
        node = root
        q.append(node)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        
        return node.val

# S: O(N)
# T: O(N)