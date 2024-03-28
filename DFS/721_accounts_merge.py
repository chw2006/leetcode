import collections

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Use a iterative graph DFS to solve this.
        # We first have to create a graph using the list of accounts.
        # Map all emails to every other connected email.
        # We also need a map to map each email to the user name. 
        # Then we do an iterative DFS on this graph and get all the accounts for each user in a sorted fashion. 

        graph = collections.defaultdict(set)
        nameMap = {}
        visited = set()
        res = []

        # Create the graph
        for a in accounts:
            # First index is always the name
            name = a[0]
            # Get the emails for this account
            for e in a[1:]:
                # We will link every email to the first email in the list as an optimization
                # Add the first email as connected to this email
                graph[e].add(a[1])
                # Add this email as connected to the first email
                graph[a[1]].add(e)
                # Map this email to the name
                nameMap[e] = name
        
        # Traverse the graph using DFS
        for email in graph:
            # We only do work if the email hasn't been visited
            if email not in visited:
                # Add email to stack
                stack = [email]
                # Set this as visited
                visited.add(email)
                # Keep track of the current result
                curr_res = []
                while stack:
                    node = stack.pop()
                    curr_res.append(node)
                    # Go through every edge in the node and add it to the stack, set it as visited.
                    for e in graph[node]:
                        if e not in visited:
                            stack.append(e)
                            visited.add(e)
                # Add the curr_res to the result, sorted.
                # Also need to add the name as the first value in the array
                res.append([nameMap[email]] + sorted(curr_res))
        
        return res

# Time Complexity: if N is the number of accounts and K is the number of emails per accounts, then the time complexity is: O(N * K * N log K).
# The N log K is for sorting the result for every email, NK is for doing DFS on the graph. 
# Space Complexity: O(NK)