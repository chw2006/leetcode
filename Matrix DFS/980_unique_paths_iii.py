class Solution:
    # Count the number of 0s in the given grid, this is what we need to hit once we reach the end.
    # Keep a visited set
    # Also keep track of current x,y coordinates.
    # Base case: when we are out of bounds, visited, or it's an obstacle, go back.
    # Base case: when we hit a cell that is 2 and we have visited enough 0s, then increment walks and return.
    # Otherwise, add to visited. 
    # Then for every direction we can go, get the new coordinates, call DFS. After the 4 calls, backtrack by removing (x, y) from visited. 
    # Return walks
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        zeroes = 0
        visited = set()
        start_x = start_y = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        # Find the number of 0s in the grid, also find out where we start
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    zeroes += 1
                elif grid[r][c] == 1:
                    start_x = r
                    start_y = c
        
        def dfs(x, y):
            # Check if we are in bounds, been visited, or this block is an obstacle.
            if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) in visited or grid[x][y] == -1:
                return 0
            # If we reach the end and visited has all the zeroes (zero + 1 because we count the starting 1)
            if grid[x][y] == 2 and len(visited) == zeroes + 1:
                # Return 1 to add 1 to walks
                return 1
            # Add to visited set
            visited.add((x, y))
            # Try to go in all 4 directions
            walks = 0
            for n_x, n_y in directions:
                walks += dfs(x + n_x, y + n_y)
            # backtrack
            visited.remove((x, y))
            return walks
        
        # Start the dfs at the starting x,y coordiante
        return dfs(start_x, start_y)
    
# T: O(4^(M * N)) - We have to call DFS in 4 directions for possibly every single cell. 
# S: O(M * N) - we have to keep a visited set that could span O * M 