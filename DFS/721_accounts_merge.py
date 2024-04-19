class Solution:
    # Create an adjacency list of email -> neighboring emails
    # Also keep a map of which emails belong to which names
    # Create the graph by mapping the first email of each account to every other email in the account and vice versa.
    # Also map email -> name in email_names
    # Iterate through the emails in the graph and for each email, get its name and then perform a DFS on that email if it's not visited.
    # The DFS simply adds the email to visited and local res. Then for each edge, if it is not visited, call DFS on it and extend result.
    # Once we get the associated emails for that email we need to add it to the result with the name first and the emails in sorted order.

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Create a graph of email -> neighboring emails. 
        # Also keep track of which name each email belongs to.
        graph = defaultdict(set)
        email_names = {}
        visited = set()
        
        # DFS: add email to visited and result. Call DFS on neighbors if they haven't been visited.
        def dfs(email):
            visited.add(email)
            res = []
            res.append(email)
            for edge in graph[email]:
                if edge not in visited:
                    # Need to do extend here so we don't add the results as a separate nested list
                    res.extend(dfs(edge))
            return res

        # Create an adjacency list for each email
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email = account[i]
                # To save space, we only want to link the first email to the rest of the emails and not all of them to each other.
                graph[account[1]].add(email)
                graph[email].add(account[1])
                email_names[email] = name
        
        res = []
        # Traverse the graph
        for email in graph:
            name = email_names[email]
            # Only call DFS on this email if it hasn't been visited
            if email not in visited:
                res.append([name] + sorted(dfs(email)))

        return res

# T: if N is number of accounts and K is emails per user, then we need to travers O(NK) when we traverse the graph. W
# We then need to sort the accounts, which takes N log K time. So final time is O(KN^2logK)
# S: We must store at least all all emails for all accounts, which is O(NK)

def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Build the graph mapping courses to its pre-reqs
    # Then go through the graph using topological sort
    # To use topological sort, we use 3 sets.
    # White set contains all nodes at the start
    # Gray set contains only the current node we are processing
    # Black set contains nodes we're done processing
    # If an edge is in gray, we have a cycle. 
    # If an edge is in black, we can skip processing it since we know we're done.
    # After processing node, remove from gray and add to black. 
    graph = defaultdict(list)
    # Create a graph
    for p in prerequisites:
        prereq = p[1]
        course = p[0]
        graph[course].append(prereq)

    # Use topological sort to traverse graph
    white = set(graph.keys())
    gray = set()
    black = set()

    def dfs(node):
        # Add node to gray set since we are processing
        gray.add(node)

        # Traverse its neighbors
        for edge in graph[node]:
            # If an edge is in the gray set, we have a cycle
            if edge in gray:
                return False
            # If an edge is in black, it's already been processed so we can skip
            if edge in black:
                continue
            # Call DFS on the edge
            if not dfs(edge):
                return False
        # Remove current node from gray since we're done with it
        gray.remove(node)
        # Add to black to show that we've processed it
        black.add(node)

        return True

    # Go through each node in graph
    for node in white:
        # For each node in white, call DFS
        if not dfs(node):
            return False
    
    return True
