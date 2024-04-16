class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Create an adjacency list from the edges in prerequisites, then run DFS.
        # Using DFS, we must visit at least every course, even one without pre-reqs. 
        # If a course does not have any pre-reqs we can take it. 
        # If it does, we need to make sure those pre-reqs can be taken and they do not have cycles.
        # Use a hash set to keep track of visited nodes, so we don't visit a node more than once. If we do, we have a cycle, return false.
        # We must use a while loop to go through all courses, in case courses are not dependent upon each other. 
        
        # Create an adjacency list for each node
        adjList = {}
        for i in range(numCourses):
            adjList[i] = []
        # Create an adjacency list using the edges (prerequisites)
        for course, prereq in prerequisites:
            adjList[course].append(prereq)
        # Use a visited set to detect cycles
        visited = set()
        # Run DFS on this adjacency list
        def dfs(i):
            # Cycle detected
            if i in visited:
                return False
            # Empty adjacency list means this course has no pre-reqs, we can take it. 
            if not adjList[i]:
                return True
            # Add to visited
            visited.add(i)
            # Visit all the prereqs
            for prereq in adjList[i]:
                # Only return false if we have a cycle
                if not dfs(prereq):
                    return False
            # Backtrack
            visited.remove(i)
            # Set adjacency list to empty to reduce work in the future
            adjList[i] = []
            # If it gets this far, we can take this course
            return True

        # Call dfs for all courses
        for i in range(numCourses):
            # Immediately return false if we have a cycle
            if not dfs(i):
                return False
            
        # All courses can be taken
        return True

# T: O(N) where N is the number of courses. Because we use a visited set, we do not visit anything more than once. 
# S: O(N) to store the graph. 