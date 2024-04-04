class Solution:
    # Base case: we're not in bounds or we've been visited or the square is 1. Return 0.
    # Base case: we've reached the end, return 1. 
    # Otherwise, add to visited set. 
    # Do DFS right and down, add to walks.
    # Backtrack by removing from visited.
    # Return walks
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = {}
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        visited = set()

        def dfs(x, y):
            # If not in bounds or visited or grid is obastacle, return 0
            if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) in visited or obstacleGrid[x][y] == 1:
                return 0
            if x == rows - 1 and y == cols - 1:
                # We've found a unique path
                return 1
            if (x, y) in cache:
                return cache[(x, y)]
            # Add to visited
            visited.add((x, y))
            # Move down or right
            walks = 0
            # Go down
            walks += dfs(x + 1, y)
            # Go right
            walks += dfs(x, y + 1)
            # backtrack
            visited.remove((x, y))
            cache[(x, y)] = walks
            return walks
        
        return dfs(0, 0)

# T: O(2^(M * N)) - Worst case, it could be better since we are caching.
# S: O(N * M) - Worst case, we visit every square in the grid in our set