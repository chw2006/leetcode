class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # To do this, we need to calculate the prefix sum during our run, not before.
        # The idea is to keep the number of occurences of a prefix sum in a hash table.
        # You calculate the rolling prefix sum and subtract k to find the difference between your current sum and k. 
        # Then you look up the difference in the hash map to see how many prefixes you can remove that can get you to k. 
        # If there are any prefixes that is equal to the difference, then that is how many occurences of the sum k in your current subarray. 

        prefixTable = {}
        # Set this to 1, since we can assume that there is a 0 value before the very first element in teh array
        prefixTable[0] = 1
        count = 0
        prefixSum = 0
        # Calculate the prefix sum as we go
        for i in range(len(nums)):
            prefixSum += nums[i]
            # Find the difference between the running sum and k. 
            diff = prefixSum - k
            # Look up the difference in the table, if there are occurences, add them to the count.
            # We look for the difference because if a difference exists already in the map, then that means there is a subarray that sums up to k. 
            count += prefixTable.get(diff, 0)
            # Increment the number of times this prefixSum has occured in the table
            prefixTable[prefixSum] = prefixTable.get(prefixSum, 0) + 1
        return count

# Meta's variation of this question asks us to return whether the subarray sum equaling to K exists in the array
# It does not ask for the number of occurences.
# This makes the problem easier, although it is mostly the same.
# Instead of using a map, we can use a set since we do not care how many occurences we have.
# Whenever we find a value in the set that is equals to current prefix sum - k, we can return True.
def metaSubarraySum(nums, k):
    prefixSet = set()
    # Add 0 to the set so if the first value is equal to k, we can return True
    prefixSet.add(0)
    total = 0
    for i in range(len(nums)):
        # Keep a running tally
        total += nums[i]
        # If prefix - k is in the set, we can return True.
        # This is because we know that for a prefix sum, if the current prefix - previous prefix = k, then we have a subarray that sums to k. 
        if total - k in prefixSet:
            return True
        # Otherwise, add this sum to the set
        prefixSet.add(total)
    # We have not found anything that sums to k
    return False

# T: O(N) - we must traverse the entire array
# S: O(N) - we keep a hash set

nums = [23, 5, 4, 7, 2, 11] 
print(metaSubarraySum(nums, k)) # True
nums = [1, 3, 5, 23, 2]
k = 7
print(metaSubarraySum(nums, k)) # False
