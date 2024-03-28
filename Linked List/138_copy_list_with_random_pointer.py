"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Go through the linked list and create deep copy nodes for each new node.
# Map the old node to the new nodes using a hash map. Do not copy the random or next pointers.
# Go through the linked list again, this time, link the new nodes together. 
# Use the old random pointer in each node to find the new random pointer node. Then link that as the new node's random.
# return the new head. 

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_map = {}
        curr = head
        
        # Create new deep copies of the node and map them old node -> new node
        while curr:
            new_node = Node(curr.val)
            node_map[curr] = new_node
            curr = curr.next
        
        # Now link the nodes
        curr = head
        while curr:
            # Get the new node
            new_node = node_map[curr]
            # Get the new next and random nodes.
            nxt_node = None
            if curr.next:
                nxt_node = node_map[curr.next]
            rnd_node = None
            if curr.random:
                rnd_node = node_map[curr.random]
            # Link next and random
            new_node.next = nxt_node
            new_node.random = rnd_node
            curr = curr.next
        
        return node_map[head]

# Time Complexity: O(N), we have to iterate through the list twice, so it's O(2N), but constants don't matter
# Space Complexity: O(N), we have to store all the nodes using a hash map. 