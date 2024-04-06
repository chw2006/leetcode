# In this variant, k can start at 0. 
import random


def findKthLargest(nums, k):
    # We are going to use quick select.
    # We need a start and end pointer for our window. 
    # We first partition the nums array based on the pivot.
    # The pivot is choosen randomly.
    # Swap the pivot with the value at the end of the array. 
    # If a value is smaller or equal to the pivot, swap it the left pointer.
    # After all values smaller than pivot are to the left of it, swap end and left.
    # After finding the partition index, if that index is equal to len(nums) - k - 1, this means we've found the value.
    # This is because the kth largest means that the element is k values away from the largest value in the array. 
    # len(nums) - 1 is the right index and k here is the left boundary. 
    # If partition index is greater than len(nums) - k - 1, then we need to move left. Set end to pi - 1.
    # If partition index is less than len(nums) - k - 1, then we need to move right. Set start to pi + 1. 
    def partition(left, right):
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]
        # Swap the pivot with right
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        partition_index = left
        # Go through the array and swap elements smaller or equal to the pivot
        for i in range(left, right):
            if nums[i] <= pivot:
                # Swap the value with partition_index
                nums[i], nums[partition_index] = nums[partition_index], nums[i]
                partition_index += 1
        # At the end of the loop, swap partition_index with right
        nums[right], nums[partition_index] = nums[partition_index], nums[right]
        return partition_index
    
    left = 0
    right = len(nums) - 1
    while nums:
        p_index = partition(left, right)
        if p_index == len(nums) - k - 1:
            return nums[p_index]
        elif p_index > len(nums) - k - 1:
            # Move left
            right = p_index - 1
        else:
            # Move right
            left = p_index + 1

nums = [3,2,1,5,6,4]
k = 2
print(findKthLargest(nums, k))  # Should be 4
nums = [3,2,3,1,2,4,5,5,6] 
k = 4
print(findKthLargest(nums, k)) # Should be 3
    
    