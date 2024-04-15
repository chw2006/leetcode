class Solution:
    # We can partition the subarray up to k.
    # So at each index, we can either partition the subarray or not partition the subarray as long as it is less than k.
    # We can keep a tally of the sum of the partition. We also need to keep the max value we've seen and current window size. 
    # When we call DFS, we want to call it on the next index and add it to the current sum, which is cur_max * window. 
    # And we only want to set it as res if it is larger than the current res. 
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        # Use a cache to memoize
        cache = {}

        def dfs(i):
            # Base case, if we reach the end of the array return 0
            if i >= len(arr):
                return 0
            # If we have this in cache, return it
            if i in cache:
                return cache[i]
            # Keep track of the current max and result
            curr_max = 0
            res = 0
            # Go through all the ways we can partition the array up to i + k
            for j in range(i, min(len(arr), i + k)):
                # Get the max we've seen so far and the window size
                window_size = j - i + 1
                curr_max = max(curr_max, arr[j])
                # Multiply these 2 and add the ensuing dfs results to get the curr_sum
                curr_sum = (window_size * curr_max) + dfs(j + 1)
                # We only set curr_sum as result when it's larger than any previous result
                res = max(curr_sum, res)
            # Cache result
            cache[i] = res
            return res

        return dfs(0)

# T: O(N * K) If N is the number of elements in the array and K is the max length of the subarray.
# This is because we have k choices for the size of the subarray and we have to at most traverse N times (for subarray sized 1). 
# The recursive part of this is simplified because we are memoizing any repeated work. 
# S: O(N) - we must store at most N elements in cache for the size of the array. 