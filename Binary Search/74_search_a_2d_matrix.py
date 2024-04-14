class Solution:
    # This is binary search in a 2D matrix.
    # We start off searching between every cell. # Find the mid row between 0 and m. 
    # Get the first and last value of that row. 
    # If the value is in between first and last, search that row. 
    # When searching that row, use binary search to search for the value. When we find it return true. If it is not there, return False. 
    # If the value is larger than last, set left to mid + 1. 
    # If the value is smaller than first, set right to mid - 1. 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m - 1

        # Search for target within one row
        def binarySearch(row):
            nums = matrix[row]
            l = 0
            r = n - 1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            
            return False

        # Search rows using binary search
        while left <= right:
            mid = left + (right - left) // 2
            # Find the first and last element in the array, we know that first is always larger than the previous last.
            first = matrix[mid][0]
            last = matrix[mid][n - 1]
            # If target is in between first and last, search this row.
            if first <= target <= last:
                return binarySearch(mid)
            # If target is larger than last value, it has to be in a next row
            elif target > last:
                left = mid + 1
            # If target is smaller than first, it has to be in a previous row
            elif target < first:
                right = mid - 1
        
        return False

# T: O(log(M*N)) - We do binary search on m rows and then binary search again on a row. 
# S: O(1) - We only use pointers