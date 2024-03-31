from math import sqrt

class Solution:
    # Go through the array, if the point shares x or y, then we calculate its manhattan distance.
    # If the distance is the smallest we've seen so far, set it to nearest_distance. Update nearest_index. 
    # If the shortest_distance is the same, only update shortest_index if the index is smaller. 
    def nearestValidPoint(self, x, y, points):
        nearest_distance = float('inf')
        nearest_index = -1
        for i in range(len(points)):
            point = points[i]
            curr_x = point[0]
            curr_y = point[1]
            # If the point is valid, calculate its manhattan distance
            if curr_x == x or curr_y == y:
                distance = abs(curr_x - x) + abs(curr_y - y)
                # If the current distance is smaller than the nearest distance, set it as nearest_distance and update its index
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_index = i
                # If this distance is equal to the nearest distance, only update its index if i is smaller than the previous nearest index
                elif distance == nearest_distance:
                    if i < nearest_index:
                        nearest_index = i
        
        return nearest_index

# T: O(N) - have to traverse the array
# S: O(1) - we only keep pointer vars
    
# There is a meta variation of a similar but much more difficult problem. It asks this:
# Given r and N, print (x,y) coordinates of N points which would lie on a circle with radius r, centered at origin.
# We know that the euclidean distance is how we measure the distance between 2 points in a 2D grid.
# In this case, we want the points to be distance r away from the origin (x, y). 
# We also know that we want a circle and a circle's bounds are x1 - r and x1 + r. 
# So what we know the X values we need to iterate through.
# Because we want n points and the x is between -r and + r, we know that it spans a distance of 2r.
# For every x value, there will be 2 y values, so the interval we want is every 4r/n. 
# To find the y value associated with every x value, we need to use this equation:
# y2 = sqrt(r**2 - (x2 - x1)**2). Then we need to add or subtract that y from the origin y to get the y values.
# Only caveat is when y is 0, then we only add 1 point. 
def getCircularCoordinates(x, y, r, n):
    left_x = x - r
    right_x = x + r
    interval = (4 * r) // n
    res = []
    # Increment x from x - r to x + r at an interval of (4 * r)/n
    for x2 in range(left_x, right_x + 1, interval):
        # Calculate the value of y
        y2 = sqrt(r**2 - (x2 - x)**2)
        # If y is 0, we only want to add 1 point
        if y2 == 0:
            res.append((x2, y))
        # Otherwise, we can add 2. 
        elif y2 > 0:
            res.append((x2, y + y2))
            res.append((x2, y - y2))
    return res

# T: O(N) - We have to iterate through at least n points. 
# S: O(N) - We have to store the results in res. It could be O(1) if we just print them as we go.
print(getCircularCoordinates(1, 2, 8, 4)) # [(0, 2), (0, -2), (2, 0), (-2, 0)]
