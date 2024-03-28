class Solution:
    # This is an expansion of 2sum
    # Because we don't want to use the same combinations, we should sort the input array.
    # Because of that, if we see that a combination starts with the same value as previous, we can skip it. 
    # Once we have a start to the combination, we want to find a value that negates it in the rest of the array.
    # We can use a 2 pointer solution for that since the input array is sorted.
    # If the 2 values at left and right add up and is bigger than the target, we want to move the right pointer left.
    # If it's smaller than the target, we want to move the left pointer right. 
    # If the 2 values sum up to the target, we can add that combination. 
    # For this case, we also need to move the left pointer and we want to do that until we no longer see the same value (since list is sorted)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            # If this is a repeat value of previous, we can skip
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            # Taraget is the negation of nums[i]
            target = -nums[i]
            # Start left at i + 1
            left = i + 1
            right = len(nums) - 1
            # Use 2 pointers to search for the pairs of values that will negate target
            while left < right:
                # Get the total of the 2 values
                total = nums[left] + nums[right]
                # If it's equal to target, we can add it to the result
                if total == target:
                    res.append([nums[i], nums[left], nums[right]])
                    # We need to only move one pointer here
                    left += 1
                    # And we need to keep moving l until we no longer see the same value
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < target:
                    # Move left pointer right
                    left += 1
                elif total > target:
                    # Move right pointer left
                    right -= 1
        return res

# T: O(N^2) - We have a nested loop. We also have to sort, which is O(NlogN), but the quadratic time is way bigger.
# S: O(N) - We need to keep the result