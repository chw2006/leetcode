class Solution:
    # A beautiful subset is a subset without any values that have an absolute difference of k. 
    # So any value in the set cannot be x + k or x - k also in the set. 
    # We can find the number of subsets by doing a DFS on nums.
    # We will keep a map of illegal values, or values that cannot be added to the subset because of the x +/- k limitation.
    # The base case is that we've reached the end of the string, so this is a subset. Return 1. 
    # For any value we can decided to either take it or not take it.
    # If the value is not illegal, we can take the subset by adding its illegal values to the illegal_values dictionary. 
    # If we do not take it, we don't add to the illegal values.
    # Return the dfs call - 1 since we want to exclude the empty subset
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        illegal_values = collections.defaultdict(int)

        def dfs(i):
            # Base case: if we've reached the end, we have a valid subset
            if i == len(nums):
                return 1
            subsets = 0
            # If this value is not illegal, add this value to the subset
            if illegal_values[nums[i]] == 0:
                # Add the illegal values to the subset
                illegal_values[nums[i] + k] += 1
                illegal_values[nums[i] - k] += 1
                # Take this value
                subsets += dfs(i + 1)
                # Backtrack and remove the illegal values
                illegal_values[nums[i] + k] -= 1
                illegal_values[nums[i] - k] -= 1
                
            # Don't take this value
            subsets += dfs(i + 1)
            
            return subsets
        
        # Return dfs - 1 because we want to exclude the empty subset
        return dfs(0) - 1