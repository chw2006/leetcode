# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Similar problem to #314, but in this case I think we need to keep track of the y values as well. 
        # We want to print the nodes by column.
        # So we want to do a BFS on this tree and assign each node an x and y coordinate. 
        # We keep track of the nodes for each x coordinate in a map. The values are the node value along with its y coordinate. 
        # The root starts at x = 0. The left child is x - 1. The right child is x + 1. 
        # We also need to keep track of the max and min x values we see. 
        # This is so we can then iterate through the map to generate the result. 
        # When we iterate through the map using the x range, we have to sort each list by its y value and then by its node value (for when y value is same)
        # Add only the node values to a list and adds those to the result. 

        if not root:
            return []
    
        # Queue for BFS. We put in the coordinate and the first node
        q = deque([(0, 0, root)])
        # Min/max values
        min_x = float("inf")
        max_x = -float("inf")
        # Map for each coordinate
        map = defaultdict(list)
        res = []
        
        while q:
            for _ in range(len(q)):
                # Pop from the queue
                x, y, node = q.popleft()
                # Add this to the map
                map[x].append((node.val, y))
                # Update the min/max x values we've seen so far
                min_x = min(min_x, x)
                max_x = max(max_x, x)
                # If there's a left child, decrement x
                if node.left:
                    q.append((x - 1, y + 1, node.left))
                # If there's a right child, increment x
                if node.right:
                    q.append((x + 1, y + 1, node.right))
        
        # Go through the map using min_x and max_x and add the to the results
        for l in range(min_x, max_x + 1):
            items = map[l]
            # Sort by the y values first, and then the node values themselves
            items.sort(key = lambda x: (x[1], x[0]))
            # Create a new list that only takes the first item in the tuple (the node values)
            items = [val for val, _ in items]
            res.append(items)
        
        return res