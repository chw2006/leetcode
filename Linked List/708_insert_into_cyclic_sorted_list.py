class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# Iterate through the list until we get to the node before the head node.
# If the value to insert is in between the current and next values, insert it there and return the head.
# If we hit the end of the list (node before head), we insert the node if it is larger than current or smaller than next.
# Lastly, if we don't return within the loop, that means all values are the same. Just insert into list.
def insert_into_cyclic_sorted_list(node, value):
    # Edge case: if node is None, create a new node with value and return it. 
    if not node:
        new_node = Node(value)
        new_node.next = new_node
        return new_node
    
    curr = node
    while curr.next != node:
        # If the node value is in between current and next, insert it
        if curr.val <= value <= curr.next.val:
            new_node = Node(value, curr.next)
            curr.next = new_node
            return node
        # We are at the end of the list (cyclical part)
        elif curr.val > curr.next.val:
            if value >= curr.val or value <= curr.next.val:
                # We have to add this to the end of the list. 
                new_node = Node(value, curr.next)
                curr.next = new_node
                return node
        curr = curr.next
    
    # If we reached here, all value are the same, just insert the new node
    new_node = Node(value, curr.next)
    curr.next = new_node

    return node
    
node1 = Node(1)
node3 = Node(3)
node4 = Node(4)

node1.next = node3
node3.next = node4
node4.next = node1

head = insert_into_cyclic_sorted_list(node3, 2)
curr = head
while curr.next != head:
    print(curr.val)
    curr = curr.next
print(curr.val)

# Time Complexity: O(N) go through list once.
# Space Complexity: O(1)



