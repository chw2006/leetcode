class Solution:
    # Use binary search to find the window
    # Left is 0, right is len(arr) - k. This is because the start of the window cannot be more than len(arr) - k. 
    # We then calculate the mid. We want to see if x is closer to the start of the window or the end of the window.
    # To find the distance between x and the start of the window we use x - arr[mid].
    # To find the distnace between x and just outside the window, we use arr[mid + k] - x
    # If the start distance is closer than the end distance, we want to move the window left. 
    # Otherwise, we want to move the window right. 
    # Once we break out of the loop and find the start of the window, return arr[left:left + k]
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        # Right is len(arr) - k because the start of the window cannot be past this point. 
        right = len(arr) - k
        # We do not want left and right to intersect since we are using left's value in the result
        while left < right:
            mid = left + (right - left) // 2
            # Left distance is the distance beween x and mid. Since mid is supposed to be the start of the window, x is technically bigger. 
            left_distance = x - arr[mid]
            # Right distance is the distance of just outside the window
            right_distance = arr[mid + k] - x
            # If mid is closer to x than mid + k, then we go left. 
            if right_distance >= left_distance
                # Move window left.
                right = mid
            else:
                # Move the window right
                left = mid + 1
        
        return arr[left:left + k]

    # T: O(log(N - K)): This is because we use binary search along a range that is N - K elements. 
    # S: O(1)
        
