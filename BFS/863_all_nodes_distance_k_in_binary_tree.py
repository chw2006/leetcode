# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# The distance between 2 nodes is the 
class Solution:
    # Give each node in the tree an adjacency list
    # We basically turn this tree into a graph
    # Then traverse the graph starting from target and keep track of the distance
    # When distance is equal to k, add that node's value to the result. 
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # Case of k being 0, so we can only return the target
        if k == 0:
            return [target.val]
        q = deque()
        q.append(root)
        graph = defaultdict(list)
        res = []
        # Generate the graph
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    # Add mappings to graph
                    # parent -> child
                    # child -> parent
                    graph[node].append(node.left)
                    graph[node.left].append(node)
                    # Add child to queue
                    q.append(node.left)
                if node.right:
                    # parent -> child
                    # child -> parent
                    graph[node].append(node.right)
                    graph[node.right].append(node)
                    # Add child to queue
                    q.append(node.right)
        
        # Use a tuple for traversing, (node, distance)
        q = deque()
        q.append((target, 0))
        # Use a visited set so we don't have cycles
        visited = set()
        # Traverse the graph starting from target
        while q:
            for _ in range(len(q)):
                node, distance = q.popleft()
                # Set as visited
                visited.add(node.val)
                # If we hit distance k, add that node's value to result
                if distance == k:
                    res.append(node.val)
                else:
                    # Visit every neighbor for this node, but only if they haven't been visited yet
                    for edge in graph[node]:
                        if edge.val not in visited:
                            q.append((edge, distance + 1))
                            visited.add(edge.val)
        
        return res

# T: O(N) - We traverse the tree twice, but we only visit N nodes at most each time.
# S: O(N) - At worst, we must store all nodes in the queue or map. 