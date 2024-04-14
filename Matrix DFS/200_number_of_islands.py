class Solution:
    # Iterate through the matrix. If we see a "1" and it hasn't been visited, kick off a DFS and increment islands. 
    # The DFS function's main point is to add values to the visited list, so we don't visit them again if they are part of the same island.
    # We also check if the current cell is in bounds, visited, or if it's part of an island.
    # After going through every cell in the grid, return islands. 
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            # Base case
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == '0':
                return
            # Add to visited
            visited.add((r, c))
            # Call DFS on neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Go through every cell, only call DFS if the grid is an island and hasn't been visited
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    # We know this is at least 1 island
                    islands += 1
                    dfs(r, c)
        
        return islands

# T: O(M * N) - Because of the visited set, we visit at most all the cells in the grid.
# S: O(M * N) - We have to use a visited set, that takes at most O(M * N) space. 