class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Going from right to left, find the location where the array is no longer decreasing. 
        # The value to the left of that is the pivot.
        # If no pivot was found, that means the array is strictly decreasing, so we need to return the reverse. 
        # Now we look for the value that is the first value larger than the pivot to the right of it. 
        # We want to swap that value with the pivot.
        # After swapping, we need to make sure everything to the right of the pivot is in increasing order, so reverse everything to the right of pivot. 
        """
        Do not return anything, modify nums in-place instead.
        """

        pivot = -1

        # Try to find the pivot
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        # If there is no pivot, we can return the reverse of nums since the array is constantly decreasing from left to right (321 -> 123)
        if pivot == -1:
            nums.reverse()
            return
        
        # Find the swap index, starting from the end of the array
        swap = len(nums) - 1
        # The swap we are after is the first value to the right of pivot that is larger than the pivot
        while nums[swap] <= nums[pivot]:
            swap -= 1
        # Swap the 2 values
        nums[swap], nums[pivot] = nums[pivot], nums[swap]
        # Now make sure everything to the right of pivot is reversed.
        nums[pivot + 1:] = reversed(nums[pivot+1:])

        return

# T: O(N) - have to iterate once through the whole array in the worst case. 
# S: O(1) - we are doing the swaps in place