class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

# If head doesn't exist, create a new node with insertVal with its next pointing to itself and return it.
# Iterate through the list until we get to the node before the head.
# While iterating, check if the value is in between the current value and next value. If it is, insert the value there.
# If the current value is larger than the next value, then we are right before the cyclical part of the list.
# Here we need to insert the new value after current and then link the new node to curr.next. 
# If insertVal is in between current and next, but curr.val is smaller than next val, insert at end

def insert(self, head, insertVal):
    if not head:
        new_node = Node(insertVal)
        new_node.next = new_node
        return new_node
    
    curr = head
    while curr.next != head:
        # Create new node and insert it in between
        if curr.val <= insertVal <= curr.next.val:
            new_node = Node(insertVal, curr.next)
            curr.next = new_node
            return head
        elif curr.val > curr.next.val:
            # If insertVal is in between the current and next, add to end of list
            if insertVal >= curr.val or insertVal <= curr.next.val:
                new_node = Node(insertVal, curr.next)
                curr.next = new_node
                return head
        curr = curr.next

    # If insertVal is in between current and next, but curr.val is smaller than next val, insert at end
    new_node = Node(insertVal, curr.next)
    curr.next = new_node

    return head

node1 = Node(1)
node3 = Node(3)
node4 = Node(4)

node1.next = node3
node3.next = node4
node4.next = node1

head = insert(node3, 2)
curr = head
while curr.next != head:
    print(curr.val)
    curr = curr.next
print(curr.val)

# Time Complexity: O(N) go through list once.
# Space Complexity: O(1)


