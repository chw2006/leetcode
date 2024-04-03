class Robot:
   def move(self):
       """
       Returns true if the cell in front is open and robot moves into the cell.
       Returns false if the cell in front is blocked and robot stays in the current cell.
       :rtype bool
       """
       return True

   def turnLeft(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def turnRight(self):
       """
       Robot will stay in the same cell after calling turnLeft/turnRight.
       Each turn will be 90 degrees.
       :rtype void
       """
       pass

   def clean(self):
       """
       Clean the current cell.
       :rtype void
       """
       pass

def cleanRoom(robot):
    # We start at (0, 0) even though we are not given the origin of the grid.
    # We can go in four directions, up, right, down, left.
    # We need to define these directions in either a clock-wise or counter-clock-wise order.
    # We need to use a DFS helper function that takes in the current coordinates and the direction we are going.
    # We need to keep a visited set so that we don't keep cleaning the same cells.
    # For every cell we encounter, we clean it and add it to the visited set. 
    # Then we need to travel in any of the 4 directions possible.
    # We do this by iterating through the directions array and seeing if that new direction is in bounds or has been visited.
    # If we can move there (in bounds) and has not been visited, call dfs with the new coordinates and new direction.
    # We always try to move in a clock-wise direction so that for the loop, we change the direction 90 degrees.
    # After calling DFS, we need to backtrack, which turns the robot backwards, moves, and then turns twice again.
    # We always want the robot to be facing up for each dfs call.  

    # Go in clock-wise order. Up, right, down, left.
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    def backtrack():
        # Point the robot backwards
        robot.turnRight()
        robot.turnRight()
        robot.move()
        # turn right twice to get the robot to point up again
        robot.turnRight()
        robot.turnRight()

    def dfs(x, y, direction):
        # Clean this current tile
        robot.clean()
        # Add to visited
        visited.append((x, y))

        # Find the next tile to move to
        for i in range(len(directions)):
            # Directions: 0 -> up, 1 -> right, 2 -> down, 3 -> left
            # We mod 4 because direction is going to be larger than 4 eventually
            new_direction = (i + direction) % 4
            # Find new coordinates
            new_x = x + directions[new_direction][0]
            new_y = y + directions[new_direction][1]
            # If new coordiantes are in bound and we can move there
            if (new_x, new_y) not in visited and robot.move():
                # Call DFS on the new coordinates with the new direction
                dfs(new_x, new_y, new_direction)
                # Backtrack after DFS
                backtrack()
            # Turn the robot to synchronize it with the direction it's going next
            robot.turnRight()
    # Start at 0, 0 with the robot pointed up (0)
    dfs(0, 0, 0)

# T: O(N - M), where N is the number of rooms and M is the obstacles.
# S: O(N - M), we keep a visited set of only the rooms we visit, not the obstacles.
    

# Meta has a variation of the Robot vaccum cleaner problem where it uses a mouse API instead
# This can move in a certain direction (instead of just move), so we don't need to turn the mouse ourselves.
# hasCheese() returns whether or not the location has cheese a clean function.
# getCheese() needs to be implemented. Return true if cheese found and leave at mouse location with cheese
# If no cheese, then return the mouse back to where it started and return False
class Mouse:
    # Moves to one of the directions (left, right, up, down) and returns false if you can't move and true if you can.
    def move(self, direction):
        return True
    # Returns true if there is a cheese in the current cell.
    def hasCheese(self):
        return True
    # Should return true and leave the mouse at that location or false if we can't find cheese and return the mouse back to where it started.
    def getCheese(self):
        self.visited = set()
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        return self.dfs(0, 0, 0)
    
    def backtrack(self, direction):
        # If we're going up, go down to go back
        if direction == 0:
            self.move(2)
        # If we're going right, go left to go back
        elif direction == 1:
            self.move(3) 
        elif direction == 2:
            self.move(0)
        elif direction == 3:
            self.move(1)

    def dfs(self, x, y, direction):
        # Check if this current spot has cheese.
        if self.hasCheese():
            return True
        self.visited.add((x, y))
        # Iterate through all possible directions we can go
        for i in range(len(self.directions)):
            # Find new direction, mod 4 because direction can go over 4. 
            new_direction = (direction + i) % 4
            # Find the new x and y coordinates
            new_x = x + self.directions[new_direction][0]
            new_y = y + self.directions[new_direction][1]

            # If the new coordinate are not in visited and we can move in the new direction
            if (new_x, new_y) not in self.visited and self.move(new_direction):
                # Call DFS on the coordinates and direction
                # If the ensuing calls return True, we can return True
                if self.dfs(new_x, new_y, new_direction):
                    return True
                # Backtrack by going in the opposite direction of where we just went
                self.backtrack(new_direction)
        # If we still haven't return true yet, we didn't find it. 
        return False
