# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # We want to do a BFS level order traversal of the tree.
    # If at any point, we see a null, we set lastLevel to true.
    # If at any point after that, we see a non-null node, we can return False.
    # If at the end of a level and lastLevel is true, the queue must not contain any valid nodes. 
    # If we don't return False while going through the tree, we can return True.
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)
        lastLevel = False
        while q:
            # If we've seen a null node and the queue has any real nodes on it, we return False
            if lastLevel and any(q):
                return False
            else:
                for i in range(len(q)):
                    node = q.popleft()
                    # If the node is None, we know this has to be the last level
                    if not node:
                        lastLevel = True
                    else:
                        # If we've seen a None node and then hit a node that is non-Null, then we can return False
                        if lastLevel:
                            return False
                        else:
                            # Add the children
                            q.append(node.left)
                            q.append(node.right)
        return True
    
    # T: O(N) technically we have to traverse every node in the tree
    # S: O(N) since we keep a queue. 
