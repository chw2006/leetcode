from collections import deque
from collections import defaultdict
class TreeNode:
    def __init__(self, val): 
        self.val = val
        self.left = None
        self.right = None

def verticalOrder(root):
    # We want to print the nodes by column.
    # So we want to do a BFS on this tree and assign each node an x coordinate. 
    # We keep track of the nodes for each x coordinate in a map. 
    # The root starts at x = 0. The left child is x - 1. The right child is x + 1. 
    # We also need to keep track of the max and min x values we see. 
    # This is so we can then iterate through the map to generate the result. 

    # Return an empty list if the root is None
    if not root:
        return []
    
    # Queue for BFS. We put in the coordinate and the first node
    q = deque([(0, root)])
    # Min/max values
    min_x = float("inf")
    max_x = -float("inf")
    # Map for each coordinate
    map = defaultdict(list)
    res = []
    
    while q:
        for _ in range(len(q)):
            # Pop from the queue
            x, node = q.popleft()
            # Add this to the map
            map[x].append(node.val)
            # Update the min/max x values we've seen so far
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            # If there's a left child, decrement x
            if node.left:
                q.append((x - 1, node.left))
            # If there's a right child, increment x
            if node.right:
                q.append((x + 1, node.right))
    
    # Go through the map using min_x and max_x and add the to the results
    for l in range(min_x, max_x + 1):
        res.append(map[l])
    
    return res

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(verticalOrder(root))
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
print(verticalOrder(root))

#T: O(N) since we go through every node in the tree. 
#S: O(N) since we keep a mapping of x to value. 





    