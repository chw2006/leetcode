from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # What we want to do is do a BST and add the right-most value on every level to the right_side list.
        # Becaue we know in a BST, the right side is visited last. 
        # A node can be viewable if there are no nodes to the right of it. So on every level, that must be the last value. 
        # Create a queue
        queue = deque()
        # Push the root onto it
        if root:
            queue.append(root)
        # Create a right side list for the values on the right side of the tree
        right_side = []
        while queue:
            currLevel = []
            for i in range(len(queue)):
                # Pop from the queue
                curr = queue.popleft()
                currLevel.append(curr.val)
                # Add the children onto the queue
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            # Add the last value in the current level onto right_side
            right_side.append(currLevel[-1])
        return right_side