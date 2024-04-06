class Solution:
    # Use Binary Search
    # Calculate the mid, to determine which way to go, calculate the amount of missing numbers to the left.
    # The formula to calcualte the missing numbers is arr[mid] - mid - 1. 
    # If missing numbers < k, set left to mid + 1.
    # If missing numbers > k, set right to mid - 1.
    # After breaking out of the loop, take the right pointer add k + 1 to it and that is the missing number.
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            # Find the number of missing numbers to the left of mid
            missing = arr[mid] - mid - 1
            # If missing < k, go right
            if missing < k:
                left = mid + 1
            # Otherwise go right
            else:
                right = mid - 1
        
        # left pointer is the boundary in this case. 
        # If k is within the range of values given, then the left pointer will point to the last index before the kth value.
        # If k is out of the range of values given ,the the left pointer will point to the last value in the array. Kth value will be that + k
        return left + k
    
# T: O(logN) since we are using binary search
# S: O(1) since we only keep a left and right pointer
