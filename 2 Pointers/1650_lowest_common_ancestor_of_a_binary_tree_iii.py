class Node:
    def __init__(self, val, parent):
        self.val = val
        self.left = None
        self.right = None
        self.parent = parent

# There is a solution using a set
# There is also a 2 pointers solution similar to fast/slow pointers

# Set solution
def set_solution(p, q):
    ancestors = set()

    # Go through p until we hit the root and add nodes to the set
    while p.parent:
        ancestors.add(p.parent)
        p = p.parent
    # Go through q until we see a node that's already in the set. That is the LCA
    while q.parent:
        if q.parent in ancestors:
            return q.parent
        q = q.parent
        
    return None
# T: O(N) - Must at worst, traverse all nodes.
# S: O(N) - Set could at worst contain all nodes. 

# 2 pointers solution
def two_pointers(p, q):
    # Create a copy of p and q. We will use these as pointers. 
    P = p
    Q = q

    # Try to go to the parent of each node until they are equal
    while P != Q:
        # Try to get to the root of P. Once we cannot go to any more parents, reset it to q. 
        if P.parent:
            P = P.parent
        else:
            P = q
        # Try to get to the root of Q, once we can't get any more parents, reset it to p.
        if Q.parent:
            Q = Q.parent
        else:
            Q = p
    # This works because if there is a level difference between the nodes,
    # Resetting it to the other node will eventually make up that difference.
    # Kind of like a fast/slow pointer algorithm. 
    
    return P
# T: O(N) - Must traverse all nodes at worst.
# S: O(1) - This only uses pointers. 

if __name__ == "__main__":
    # Create a binary tree
    root = Node(1, None)
    root.left = Node(2, root)
    root.right = Node(3, root)
    root.left.left = Node(4, root.left)
    root.left.right = Node(5, root.left)
    root.right.left = Node(6, root.right)
    root.right.right = Node(7, root.right)

    # Find the lowest common ancestor of nodes 4 and 5
    p = root.left.left
    q = root.left.right
    ancestor = set_solution(p, q)
    print(ancestor.val)

    # Find the lowest common ancestor of nodes 4 and 7
    p = root.left.left
    q = root.right.right
    ancestor = two_pointers(p, q)
    print(ancestor.val)
