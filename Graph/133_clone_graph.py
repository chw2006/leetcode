"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # Do a DFS traversal of the graph.
    # Use a map to keep track of all the copied nodes.
    # In the DFS function, copy the current node and add it to the copied map. 
    # If the value already exists in the clone map, return that. 
    # Then for each neighbor, clone the neighbor and add it to the copied node's neighbors. 
    # Once we're all done, return the copied node.
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def clone(v):
            if not v:
                return None
            # If we already have this in the map, return that.
            if v.val in clones:
                return clones[v.val]
            # Copy the node and add it to the clone map
            copy = Node(v.val)
            clones[v.val] = copy
            # For each neighbor, add the clone of it to the copy
            for neighbor in v.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node)

# T: O(N) have to traverse all nodes and make copies of them at least once.
# S: O(N) we keep all the copied nodes in a map