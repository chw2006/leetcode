class Solution:
    # This is a matrix DFS problem
    # We can make this easier by going through the grid and keeping track of how much area is in each existing island using DFS.
    # When we see an island, we assign it its own island id (starting at 2). 
    # We then store the island id in a hash map and map it to its area.
    # Then we go through the grid again, this time only looking for 0 values we can flip. Then from that value, we take a look at the surrounding cells.
    # If the surrounding cell contains an island, we get that island's id and add it it to the surrounding set.
    # Then we go through the surrounding set and add the area of all the surrounding islands to 1 (the cell we are flipping).
    # If this area is larger than the max seen so far, set it to the new max. 
    # Edge case: if the max area at the end is 0, it means the whole grid is an island. Return the size of the grid. 
    # To do DFS to find the island's max area, make sure the cell is in bounds and is a 1. When that is the case, add 1 to the area. Then call DFS in all 4 directions.
    # Otherwise, return 0. 
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        self.area_map = {}
        self.island_id = 2
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0

        # DFS function to find the area of an island starting at row, col
        def find_area(row, col):
            # If we are in bounds, do work
            if (0 <= row < n) and (0 <= col < n) and grid[row][col] == 1:
                # Set this to the new island id
                grid[row][col] = self.island_id
                area = 1
                # Call DFS in all 4 directions
                for dr, dc in self.directions:
                    nr = row + dr
                    nc = col + dc
                    # Add to the area
                    area += find_area(nr, nc)
                return area
            else:
                # Out of bounds
                return 0

        # Go through the the grid and map the islands to area
        for r in range(n):
            for c in range(n):
                # If the grid we encounter is part of an island, call DFS to calculate its area.
                if grid[r][c] == 1:
                    area = find_area(r, c)
                    self.area_map[self.island_id] = area
                    self.island_id += 1
        
        # Go through the grid and look for 0 values. 
        for r in range(n):
            for c in range(n):
                # If the grid is a 0, we can flip it to a 1 and see if we can find a max area
                if grid[r][c] == 0:
                    curr_area = 1
                    # Use a set to add the neighbor ids, since we do not want dupes
                    neighbors = set()
                    # Go in all 4 directions and see if the neighbors are islands
                    for dr, dc in self.directions:
                        nr = r + dr
                        nc = c + dc
                        # Make sure we are in bounds
                        if (0 <= nr < n) and (0 <= nc < n):
                            curr_id = grid[nr][nc]
                            if curr_id > 1:
                                neighbors.add(curr_id)
                    # Go through all neighbors and add their area to the total
                    for neighbor in neighbors:
                        curr_area += self.area_map[neighbor]
                    # Update max area
                    max_area = max(curr_area, max_area)
        
        # Edge case: if max area is still 0, that means the grid is all 1s.
        if max_area == 0:
            return n * n
        else:
            return max_area

# T: O(N^2) - We have to make 2 passes through the entire N x N grid
# S: O(N^2) - We have to keep an area map and worst case is that every other grid is an island that we'd have to store. So we'd have to store N^2/2, which is still N^2.
