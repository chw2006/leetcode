class Solution:
    # Have one pointer iterate thrugh nums
    # Have another pointer point to where we are placing non-zeroes
    # If p1 is non-zero, place at p2. Increment both
    # If p1 is zero, only increment p1. 
    # After first pass-through, p2 + 1 is where we need to insert 0s.
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Start both pointers at 0
        p1 = 0
        p2 = 0
        # Iterate through the array using p1 and copy all non-zero values to the front of the array
        while p1 < len(nums):
            # If we see a non-zero copy the value of p1 to p2. 
            if nums[p1] != 0:
                nums[p2] = nums[p1]
                # Increment both
                p1 += 1
                p2 += 1
            else:
                # If we see a 0, ignore it and only increment p1
                p1 += 1
        # Fill the rest of the array with 0s
        while p2 < len(nums):
            nums[p2] = 0
            p2 += 1
# T: O(N): we have to go through the entire array
# S: O(1): we only use pointers
