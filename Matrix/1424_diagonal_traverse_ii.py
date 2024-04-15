class Solution:
    # All values in a diagonal always have the same sum for their row and column. 
    # We can use this to our advantage and place all values in the arrays with the same row and col sum. 
    # We traverse from the last row to the first because that is the order designated in the problem (go from bottom left to top right)
    # After building the map, traverse it from 0 to its largest key + 1 (since range is not inclusive)
    # Add the values of each sum to the result. 
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diag_map = defaultdict(list)
        rows = len(nums)
        res = []

        # Traverse rows backwards and build the map of the diagonal values
        for r in range(rows - 1, -1, -1):
            for c in range(len(nums[r])):
                # Store each value with the key of the sum of its row and col
                diag_map[r + c].append(nums[r][c])
        
        # Get the max sum from the map's keys
        max_sum = max(diag_map.keys())
        # Go through all sums in the map and add them to the result. 
        for i in range(max_sum + 1):
            # Need to use extend here because every value in the map is an array itself
            res.extend(diag_map[i])
        
        return res

# T: O(M * N) - where N is the length of nums and M is the max length of any array within nums. 
# S: O(M * N)  - we have to store all array values in a map and in the result