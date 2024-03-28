
def merge(nums1, m, nums2, n):
    # nums1 is going to store the result, thus we need to put nums2 into nums1. 
    # Get the last element in nums1, which will be m + n - 1. 
    # Merge the 2 lists in reverse order
    # If there are any leftover elements in nums2, put it in nums1. 

    """
    Do not return anything, modify nums1 in-place instead.
    """

    last = m + n - 1
    
    # Merge in reverse in-place
    while m > 0 and n > 0:
        # If nums1 is currently larger, set last to nums1
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            # If nums2 is currently larger, set last to nums2
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    # If there are any leftover items in nums2, put them into nums1
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

# T: O(N)
# S: O(1)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # [1, 2, 2, 3, 5, 6]

nums1 = [1]
m = 1
nums2 = []
n = 0
merge(nums1, m, nums2, n)
print(nums1)  # [1]

nums1 = [0]
m = 0
nums2 = [1]
n = 1
merge(nums1, m, nums2, n)
print(nums1)  # [1]