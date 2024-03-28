class Solution:
    # Create a prefix sum array
    # Iterate through the prefix array and find the sum to the left of that value and the sum to the right
    # If the values equal, then that is the pivot index
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = []
        total = 0
        # Generate the prefix sums array
        for num in nums:
            total += num
            prefixSums.append(total)
        
        # Iterate through the array, getting the left and right sums
        for i in range(len(nums)):
            leftSum = 0
            # If i == 0, leftSum has to be 0. Otherwise it is prefix[i - 1]
            if i > 0:
                leftSum = prefixSums[i - 1]
            # rightSum is always the total sum of the array - prefix[i]
            rightSum = total - prefixSums[i]
            # If they are equal, we've found the pivot index
            if leftSum == rightSum:
                return i
                    
        # If we haven't found a pivot index yet, we have to return -1
        return -1

# T: O(N)
# S: O(N), since we must keep the prefixSums array. 