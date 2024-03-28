class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):
        # Do in order traversal. 
        # Keep track of the last node seen and the first node seen.
        # When we process a node and last is None, set it to first. 
        # Otherwise, set last's right to the current node. Set current node's left to last.
        # Since this is a circular linked list, set last's right pointer to first
        # Set first's left pointer to last. 
        
        self.first = None
        self.last = None

        def inorder(node):
            if node:
                # In order is left, root, right
                inorder(node.left)
                # Process the node
                if not self.last:
                    # Set first to this node
                    self.first = node
                else:
                    # Set last's right to the current node
                    self.last.right = node
                    # Set this node's left to last
                    node.left = self.last
                # Set last to this node
                self.last = node
                inorder(node.right)
        
        if not root:
            return None

        inorder(root)

        # Set last's right pointer to first
        self.last.right = self.first
        self.first.left = self.last
        
        return self.first

root = Node(4, Node(2, Node(1, None, None), Node(3, None, None)), Node(5, None, None))
s = Solution()
res = s.treeToDoublyList(root)
while res:
    print(res.left.val)
    print(res.val)
    print(res.right.val)
    res = res.right
    if res == root:
        break

# Time complexity: O(N)
# Space complexity: O(N)
