# This is a Meta variation of Find Peak Element.
# Instead of finding the peak, find the valley, which is a point in the array whose neighbors are both larger. 
# We can assume that any areas outside the array go to infinity.
def findValleyElement(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        curr = nums[mid]
        # If we are out of bounds, the neighbors go to infinity
        ln = float('inf')
        rn = float('inf')
        if mid > 0:
            ln = nums[mid - 1]
        if mid < len(nums) - 1:
            rn = nums[mid + 1]
        # If the current val is smaller than both neighbors, we've found a valley
        if ln > curr and rn > curr:
            return mid
        # Always go towards the smaller side.
        # This is because the array can either be monotomically increasing/decreasing or it could be all over the place.
        # If it is decreasing, then we can assume that there has to be a valley eventually because the boundaries are infinite.
        # If it is not decreasing, then there has to be a value that is larger than the left neighbor. In that case, the left neighbor would actually be a valley. 
        # Go left since left neighbor is smaller
        elif ln < curr:
            right = mid - 1
        # Go right since right neighbor is smaller
        elif rn < curr:
            left = mid + 1

# T: O(logN), since we are doing binary search
# S: O(1), since we are not using any extra space.
            
nums = [1, 2, 3, 1]
print(findValleyElement(nums)) # Should be 0 or 3. 
nums = [1, 2, 1, 3, 5, 6, 4]
print(findValleyElement(nums)) # Should be either 0, 2, or 6.

