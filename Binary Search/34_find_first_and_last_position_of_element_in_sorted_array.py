class Solution:
    # Find the index of the target using binary search
    # We need to do binary search twice.
    # The first time we do it we want to find the index of the value and then keep going left to find the left-most index with this value.
    # Then we want to do binary search again and find the right most index with this value.
    # We then return the left and right indices.
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Binary search with a bias
        # If bias is left, we want the left-most index with the target value
        # If bias is right, we want the right-most index with the target value
        def binarySearch(bias):
            l = 0
            r = len(nums) - 1
            idx = -1

            while l <= r:
                mid = (l + r) // 2
                # Once we've found the target, we keep searching based on the bias
                if nums[mid] == target:
                    idx = mid
                    # If we find the target, we will move l/r based on the bias.
                    # If we want to see what the bounds are on the left of mid, set r to mid - 1.
                    # If we want to see what the bounds are on the right of mid, set l to mid + 1.
                    if bias == 'left':
                        r = mid - 1
                    elif bias == 'right':
                        l = mid + 1
                elif nums[mid] > target:
                    # Go left
                    r = mid - 1
                elif nums[mid] < target:
                    # Go right
                    l = mid + 1

            return idx
    
        # Search for the left-most and right-most index of target
        left = binarySearch('left')
        right = binarySearch('right')
        return [left, right]
    
    # T: O(logN) - We call binary search twice, which is O(2logN), but we don't care about constants. 
    # S: O(1) - We only keep pointers. 