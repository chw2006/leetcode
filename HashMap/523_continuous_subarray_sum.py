class Solution:
    # The idea is to create a prefix sum and then go through that array.
    # When we go through that array, mod every prefix sum by k and put the remainder in a hash map with the value being the index.
    # If we reach any point where we see the same remainder, then we have hit a multiple of k. 
    # Because the problem requires that the array be at least 2 length, the current index - the index of the same remainder must be >= 2. 
    # If not, we continue. 
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        # Use a hash map to keep track of the remainders
        remainders = {}
        # Because the length must be at least 2, set the remainder of 0 to -1 so if the sum is at index 1, its length is at least 2. 
        remainders[0] = -1

        for i in range(len(nums)):
            # Calculate the running sum
            total += nums[i]
            # Mod sum by k
            r = total % k
            # If the remainder is not already in the remainders table, add it
            if r not in remainders:
                remainders[r] = i
            # If the remainder is already in the table, then we've reached a multiple of k
            else:
                # Check that the array is at least of size 2, if not continue. 
                if i - remainders[r] > 1:
                    return True
        
        return False

# T: O(N)
# S: O(N), must keep remainders map. 
