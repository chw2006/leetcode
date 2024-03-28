class Node:
    def __init__(self, key=None, val=None, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.next = nxt
        self.prev = prev

class LRUCache:
    
    # For the constructor we need to save the capacity.
    # We also need to create a cache 
    # We also need to init the LinkedList that keeps track of the LRU
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # lru is on the left side of the list, mru on the right. These are dummy nodes
        self.lru = Node()
        self.mru = Node()
        # Initially, set lru's next to mru
        self.lru.next = self.mru
        # Set mru's prev to lru
        self.mru.prev = self.lru
    # T: O(1)
    # S: O(N), we keep a cache
    
    # Insert a node as the MRU
    def insert(self, node):
        # Save the MRU's previous
        prev = self.mru.prev
        # Link the saved prev to the new node
        prev.next, node.prev = node, prev
        # Link the new node to mru
        node.next, self.mru.prev = self.mru, node
    
    # Remove the node from the LinkedList
    def remove(self, node):
        # Get the prev and next of the node to remove
        prev = node.prev
        nxt = node.next
        # Get the previous and next of node and link them to each other
        prev.next, nxt.prev = nxt, prev

    # For get, if the key doesn't exist, return -1
    # If the key exists, remove it from the list and then insert it again as MRU
    # Return the value
    def get(self, key: int) -> int:
        # We only return a value if the key exists in cache
        if key in self.cache:
            # If it exists, we have to set this as the MRU
            # So first remove it from the LinkedList and add it again
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        # If it doesn't exist, return -1
        return -1
    # T: O(1): a map lookup is constant time. Removing and adding to the list is all constant time since it's pointer manipulation.
    # S: O(1): we introduce no space. 

    # If the key already exists, update the value of the node.
    # Then set it as MRU by removing it and inserting into the list again.
    # If it doesn't exist, create a new node, add it to the cache.
    # If the cache is over capacity, remove the LRU from it and delete the LRU from the list. 
    # Insert the new node as MRU into the list. 
    def put(self, key: int, value: int) -> None:
        # If the key is already in the map, we need to update it and set it to MRU
        if key in self.cache:
            # Update the value of the node
            self.cache[key].val = value
            # Remove this node from the list
            self.remove(self.cache[key])
            # Add it as MRU
            self.insert(self.cache[key])
        else:
            # Create a new node and put it in the cache
            new_node = Node(key, value)
            # Update the cache with the new node
            self.cache[key] = new_node
            # Check if we're at capacity in cache
            if len(self.cache) > self.capacity:
                # We have to evict the LRU
                # Remove it from the map
                self.cache.pop(self.lru.next.key)
                # Remove from linked list
                self.remove(self.lru.next)
            # Now add this to the linked list as MRU
            self.insert(self.cache[key])
    #T: O(1): all lookups are constant time. Inserting/updating/removing from a map is constant time. All linked list manipulation is constant time.
    #S: O(1): no new space is allocated