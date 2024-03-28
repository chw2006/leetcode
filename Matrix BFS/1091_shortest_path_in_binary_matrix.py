class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # BFS would always return the shortest path
        # Use a queue and a visit set
        # Add the first element to the queue and the visited set.
        # Go while the queue is non empty and go through the queue.
        # Pop from the queue, if we are at the end, return the length. 
        # We can go 8 different directions, go through every one of them.
        # For every neighbor, make sure we are in bounds, it hasn't been visited, and the cell is clear. 
        # Add the neighbor to the queue and visited set. 
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        q = deque()
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        res = 1

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                # Check if we've reached the end
                if r == n - 1 and c == n - 1:
                    return res
                # We can go 8 ways, right, left, up, down, up-left, down-right, up-right, down-left
                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
                for nr, nc in neighbors:
                    # Check if the neighbor is in bounds or it's been visited or if the cell is not clear
                    if (min(r + nr, c + nc) < 0 or
                        r + nr == n or c + nc == n or 
                        (r + nr, c + nc) in visited or 
                        grid[r + nr][c + nc] == 1):
                        continue
                    # Add the neighbor to the queue and visited
                    q.append((r + nr, c + nc))
                    visited.add((r + nr, c + nc))
            res += 1
        
        return -1