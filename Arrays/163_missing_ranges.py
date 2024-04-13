class Solution:
    # There's 3 edge cases to this, but otherwise it's very straight forward.
    # For all non-edge values, we can simply compare the current to previou values.
    # If there is a difference of more than 1, then we add (prev + 1, curr - 1) to the result.
    # For the lower bound, if the first value is larger than lower, we need to add a range of (lower, first - 1)
    # For the upper bound, if the last value is smaller than upper, we need to add a range of (last + 1, upper)
    # If the list given is empty, we return the range given (lower, upper)
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        n = len(nums)

        # If the nums list is empty, return original range
        if not nums:
            res.append([lower, upper])
            return res

        # If first value is larger than lower, we need to include all values between lower and first value.
        if nums[0] > lower:
            res.append([lower, nums[0] - 1])
        
        # For all values in the middle, the difference between must be larger than 1. 
        for i in range(1, len(nums)):
            curr = nums[i]
            prev = nums[i - 1]
            if curr - prev > 1:
                res.append([prev + 1, curr - 1])
        
        # If upper is larger than last value, include all values between last and upper (inclusive for upper)
        if nums[n - 1] < upper:
            res.append([nums[n - 1] + 1, upper])
        
        return res
    
# T: O(N)
# S: O(1)