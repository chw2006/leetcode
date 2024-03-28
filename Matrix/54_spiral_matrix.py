class Solution:
    # We need to account for 4 directions and whether or not we've visited the node or not.
    # First thing to check is if i and j are in bounds. If they are not or the coordinate has been visited, we need to reset the direction. 
    # If we were going right, now go down. If we were going down, go left. If we were going left, go up. If we were going up, go right. 
    # If we are in bounds and have not been visited, add the value to the result and set it as visited. Then based on the current direction, set the coordinates. 
    # If we are going right, increment j. If we are going left, decrement j. 
    # If we are going up, decrement i. If we are going down, increment i. 
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])
        i = j = 0
        dir = "right"

        # Loop until we have all the values in the matrix in res
        while len(res) != (rows * cols):
            # Check if we are in bounds or have been visited.
            if i < 0 or i == rows or j < 0 or j == cols or (i, j) in visited:
                if dir == "right":
                    # If we're going right, now we have to go down.
                    dir = "down"
                    # If we went too far right, our j value is equal to cols.
                    # So now we need to subtract 1. 
                    j -= 1
                    # If we go down, we have to increment i. 
                    i += 1
                elif dir == "down":
                    # If we're going down, we have to go left. 
                    dir = "left"
                    # If we we went too far down, our i value = rows, so decrement i. 
                    i -= 1
                    # If we go left, we are decrementing j.
                    j -= 1
                elif dir == "left":
                    # If we're going left, we now have to go up
                    dir = "up"
                    # If we went too far up, our j value is less than 0, so increment j
                    j += 1
                    # Going up means decrementing i
                    i -= 1
                elif dir == "up":
                    # If we're going up, we now have to go right
                    dir = "right"
                    # If we went up too far, our i < 0, so increment i.
                    i += 1
                    # If we go right, we have to increment j
                    j += 1
            # Add to the result and visited
            res.append(matrix[i][j])
            visited.add((i, j))
            # Find the next cell
            if dir == "right":
                j += 1
            elif dir == "down":
                i += 1
            elif dir == "left":
                j -= 1
            elif dir == "up":
                i -= 1

        return res

# T: O(N) as we have to traverse every node. We also do not visit any nodes twice. 
# S: O(N) since we need to keep the result and a visited set. 