class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Use prefix sum and DFS.
        # Calculate the prefix sum of the nums array.
        # DFS function takes the current index and the amount of subarrays we have. 
        # Base case is if we are at 3 subarrays, return. 
        # If the length of the current index would overflow, return. 
        # We can either take the current window or not take it.
        # If we take it, call DFS with on the next windows to get their sums (increment used, increment i by k)
        # Then add our current sum to it. 
        # If we don't take it, increment i and do not increment used. 
        # Update the max sum we've seen so far and return the max values. 

        cache = {}
        prefix = []
        total = 0
        # Generate prefix sums
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)
        
        def dfs(i, used):
            # Check if we're at the 3rd array
            if used == 3:
                return 0, []
            # Check if the window would be out of bounds
            if i + k - 1 >= len(nums):
                return 0, []
            # Check if we have this in cache
            if (i, used) in cache:
                return cache[(i, used)]
            
            # We can take this sum
            take_sum, take_idx = dfs(i + k, used + 1)
            if i == 0:
                # If i is at start of array, the prefix sum is just the prefix at right
                take_sum += prefix[i + k - 1]
            else:
                # Otherwise it's the prefix at right - the one prior to left. 
                take_sum += prefix[i + k - 1] - prefix[i - 1]
            # We don't take this sum
            skip_sum, skip_idx = dfs(i + 1, used)

            # Check which one gave us a larger sum
            if take_sum >= skip_sum:
                # Set the take sum as the result
                cache[(i, used)] = (take_sum, ([i] + take_idx))
                return cache[(i, used)]
            else:
                # Set skip sum as result
                cache[(i, used)] = (skip_sum, skip_idx)
                return cache[(i, used)]

        return dfs(0, 0)[1]

# T: O(N) - Without memoization and prefix sums, this is O(2^N). But using memoization brings it down to O(N)
# S: O(N) - O(N) for the prefix sum and the used array we copy each time when we call DFS. 