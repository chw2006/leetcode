class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Use 2 pointers for this.
        # Start a left at 0, right at the end. 
        # To calculate the water that each unit can hold, we need to know the maximum value on the left so far and vice versa on the right.
        # Whichever side has a smaller maximum moves its pointer.
        # A unit is calculated as the maxLeft/Right - height[left/right]. If this value is larger than 0, add it to the result.

        left = 0
        right = len(height) - 1
        units = 0
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            # When the left wall is smaller than the right wall. 
            if maxLeft < maxRight:
                unit = maxLeft - height[left]
                # Only add this to the result if it's positive
                if unit > 0:
                    units += unit
                # Increment left and update maxLeft
                left += 1
                maxLeft = max(height[left], maxLeft)
            # When the right wall is smaller than the left wall.
            else:
                unit = maxRight - height[right]
                if unit > 0:
                    units += unit
                # Decrement right (move it left) and update maxRight
                right -= 1
                maxRight = max(height[right], maxRight)
        return units

# T: O(N)
# S: O(1)