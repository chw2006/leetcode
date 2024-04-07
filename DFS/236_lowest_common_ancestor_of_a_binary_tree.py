# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # Perform a DFS on the root node
    # If it is equal to p or q, return that node's value.
    # Go down the left subtree first and see if we can find p or q. 
    # Then go down the right subtree.
    # If we receive values from both subtrees, then return the current node as the LCA. 
    # If we receive values from only 1 of the subtrees, return that value as the LCA.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            else:
                return left or right
        
        def recursive():
            return dfs(root)

        def iterative():
            # To do this iteratively, we must find p and q. In the process, we want to see who their parents are.
            # We can do this by using a parents dictionary where we map all children to their parents. 
            # After finding p and q, we want to find all the ancestors of p and put them in a set.
            # Then we look for q in the ancestors set. If it is not in the set, iterate up q's tree until its parent is in the set.
            # That is the LCA of both p and q. 
            stack = [root]
            parents = {root: None}
            ancestors = set()

            # Find the parents of p and q, traverse until we find both nodes.
            while p not in parents or q not in parents:
                # Pop from stack
                curr = stack.pop()
                # Add the children if they exist
                if curr.left:
                    # Map child -> parent in the parents map
                    parents[curr.left] = curr
                    stack.append(curr.left)
                if curr.right:
                    parents[curr.right] = curr
                    stack.append(curr.right)
            
            # Create an ancestors set for p
            while p:
                ancestors.add(p)
                p = parents[p]

            # Keep going up q's parents until it is also one of p's ancestors. That is the LCA. 
            while q not in ancestors:
                q = parents[q]
            
            return q
        
    
    # Time complexity: O(N)
    # Space complexity: O(N), since recursive stack frames. O(1) not counting stack frames. 
