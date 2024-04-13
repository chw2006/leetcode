class Solution:
    # Use a sliding window to solve this. 
    # Keep number of zeroes seen and max length. 
    # If a number is 0, increment zeroes. 
    # If number of zeroes is larger than k, then we must shrink the window
    # When shrinking window, if the number at left is 0, decrement zeroes.
    # If number of zeroes is less than or equal to k, update max length
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        left = 0
        max_length = 0

        for right, num in enumerate(nums):
            # If we see a zero in the window, increment zeroes
            if num == 0:
                zeroes += 1
            
            # If zeroes is larger than k, shrink window
            if zeroes > k:
                # We can only decrement zeroes if the left is a 0
                if nums[left] == 0:
                    zeroes -=1
                left += 1
            else:
                # Otherwise, update max length
                max_length = max(max_length, right - left + 1)
        
        return max_length
    
# T: O(N) - must iterate through every value in array
# S: O(1) - only using counters and pointers