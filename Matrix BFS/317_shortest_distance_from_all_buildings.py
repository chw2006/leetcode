from collections import deque

# We want to figure out the distance of each empty plot to the rest of the buildings.
# We can do this by starting from every building and traversing to every plot of land (BFS)
# We can keep a separate grid just to keep the cumulative distances of that plot to every house. 
# Usually in BFS, we would need a visited set so we don't end up stuck in an infinite loop.
# However, for this problem, that could get very space expensive as there could be a large amount of houses and each would need its own visited set.
# To alleviate this, we can decrement each cell that's been visited so that we know not to visit the cell again. 
# So for instance if we're traversing for the first house and we set a block to -1, we cannot visit that again because we think that an open space is 0. 
# However, on the next iteration, that space will be seen as empty since empty land is now designated by -1. 
# We begin by traversing the matrix to find a building we can travel from. Add it to the queue as a triplet (row, col, distance). Initial distance is 0. 
# We start BFS by popping the row, col, and distance from the queue.
# We add its neighbors to the queue, but only if the neighboring cell is in-bounds and is currently empty. 
# When adding to the queue, set distance to distance + 1.
# Also add the distance to the existing distance in the distance_grid.
# Decrement the value in the grid to designate this cell as visited. 
# Update the minimum local distance with the smallest value we've seen from the distance_grid. 
# For every new house, decrement EMPTY. 
# Also update min_distance to the local_distance. 
# If min_distance is not equal to infinity, return it. Otehrwise return -1. 
def shortestDistance(grid):
    rows = len(grid)
    cols = len(grid[0])
    # Initialize the distance grid to all 0s
    distance_grid = [[0] * cols for _ in range(rows)]
    # Define the 4 directions
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    # Constants for cell values
    EMPTY = 0
    BUILDING = 1
    min_distance = float('inf')

    # We need to traverse the grid first and look for buildings we can start at.
    for r in range(rows):
        for c in range(cols):
            # If we're at a building
            if grid[r][c] == BUILDING:
                # This is the minimum distance we've seen so far
                local_distance = float('inf')
                # Start BFS
                q = deque()
                # Add this cell to the queue along with the distance traveled. 
                q.append((r, c, 0))
                while q:
                    # Get the current cell
                    curr_row, curr_col, distance = q.popleft()

                    # Add each neighbor to the queue.
                    for row_dir, col_dir in directions:
                        next_row = curr_row + row_dir
                        next_col = curr_col + col_dir
                        # Make sure the new cell coordinates are in bounds
                        if next_row >= 0 and next_row < rows and next_col >= 0 and next_col < cols and grid[next_row][next_col] == EMPTY:
                            # Add neighbor to the queue with distance + 1
                            q.append((next_row, next_col, distance + 1))
                            # Increment this in the distance grid by distance + 1
                            distance_grid[next_row][next_col] += distance + 1
                            # Decrement this by 1 to set as visited
                            grid[next_row][next_col] -= 1
                            # Update the minimum distance seen so far
                            local_distance = min(local_distance, distance_grid[next_row][next_col])
                # We're done with this 1 building, so decrement EMPTY since we are using that as our visited set
                EMPTY -= 1
                # Update min_distance
                min_distance = local_distance
    # If min_distance is still infinity return -1 since tht means we could not find a path.
    if min_distance != float('inf'):
        return min_distance
    else:
        return -1

# T: O(N^2 * M^2) - We have to search through the grid for buildings and then possibly travel through N * M cells. So it's N^2 * M^2.
# S: O(N * M) - We have to keep a whole separate grid to store the distance values. 

grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(shortestDistance(grid)) # Should be 7
                        




