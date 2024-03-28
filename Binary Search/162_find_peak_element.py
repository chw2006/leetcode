class Solution:
    # This isn't a straight forward binary search problem
    # We can easily find a peak using a linear search, but they want it in o(logn)
    # Even though this array isn't sorted, we can still use binary search.
    # We calculate the mid and check its value against its neighbors.
    # Whichever neighbor is larger, we choose to search in that direction.
    # This is because if the array is monotomically increasing or decreasing, then we are guaranteed to have a larger value on the side with a larger neighbor. 
    # If it is not monotomically increasing or decreasing, then it is guaranteed that there is at least one value that is larger than the current value on that side.
    # Thus guaranteeing that we will find a peak. 
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        MIN = -2147483649

        while left <= right:
            mid = (left + right) // 2
            cur = nums[mid]
            # Neighbors must be set to the absolute minimum values since values can go to -2**31. 
            ln = MIN
            rn = MIN
            # We must account for edge values. We can't subtract from mid if it's 0, that would be out of bounds.
            if mid > 0:
                ln = nums[mid - 1]
            # Same goes for anything that is larger than the size of the array. 
            if mid < right:
                rn = nums[mid + 1]
            # If current is larger than both of its neighbors, it is a peak. 
            if cur > ln and cur > rn:
                return mid
            # If the left neighbor is larger, search that way by setting right to mid - 1.
            elif ln > cur:
                right = mid - 1
            # If the right neighbor is larger, search that way by setting left to mid + 1
            elif rn > cur:
                left = mid + 1