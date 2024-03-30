class Solution:
    # Sum up every value in the array.
    # We know that there are n + 1 numbers from 0 to n
    # And there are only n values in the array.
    # So the difference in the sums of the 2 is the answer. 
    def missingNumber(self, nums):
        numSum = 0
        rangeTotal = 0

        # In one loop, we can achieve this. 
        # Add i to rangeTotal every time. 
        # Calculate the total for everything in nums. 
        for i in range(len(nums)):
            rangeTotal += i
            numSum += nums[i]

        # Because i only goes to n - 1, we have to add n to it.
        rangeTotal += len(nums)

        return rangeTotal - numSum

# T: O(N) - go through every value in nums
# S: O(1) - Only keep track of 2 counters
    
# Meta asks a variation of this question: Given an array of size n check whether the array contains numbers from 0 - (n-1).
# It has different parameters: the numbers in the array may not be unique and may contain negatives. 

def missingNumber(nums):
    # If the array contains n numbers, it must include all numbers range 0 to n - 1. 
    # Keep a counts array that uses the indicies as the key and the occurences of each number.
    # If any number is still 0 at the end, then that means nums is missing a number between 0 and n - 1.
    # This is not space optimized. 
    n = len(nums)
    counts = [0] * n
    for num in nums:
        if 0 <= num < n:
            counts[num] += 1
    if 0 in counts:
        return False
    else:
        return True

# Space optimized solution
def _missingNumber(nums):
    # We can get an O(N) solution with O(1) space. 
    # We know that in order 
    # To do this, we have to modify the array in place. If we see a number (num), use that as an index and negate the val at that index.
    # When we get the val from nums we take the absolute value of it so the negation does not matter. 
    n = len(nums)
    zero_seen = False
    for num in nums:
        num = abs(num)
        if num >= n:
            return False
        # If we see 2 zeroes, we can return False. We also have to do this because we can't negate 0. 
        if num == 0:
            if zero_seen:
                return False
            zero_seen = True
        else:
            # For values between 1 - n, check if we've seen it before by using num as an index.
            # If that value is negative, then we've seen it and we can return false
            if nums[num] < 0:
                return False
            # Negate the value at nums[num] to signal that we've seen it
            nums[num] *= -1
    # If we don't return False earlier, we can return True
    return True

nums = [6,6,4,2,3,5,7,0,1]
print(_missingNumber(nums))
