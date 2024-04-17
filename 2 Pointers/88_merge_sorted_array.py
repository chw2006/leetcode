
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

# Meta's variation of Merge sorted arrays
# It asks us to sort 3 sorted arrays into one, without any duplicates.
# It does not restrict us to do the sorting in-place. 
def mergeSortedArrays(arr1, arr2, arr3):
    res = []
    len1 = len(arr1)
    len2 = len(arr2)
    len3 = len(arr3)
    i = j = k = 0
    
    while i < len1 and j < len2 and k < len3:
        # Make sure all indices are in bounds
        val1 = float("inf")
        val2 = float("inf")
        val3 = float("inf")
        # Only assign values if indicies are in bounds
        if i < len1:
            val1 = arr1[i]
        if j < len2:
            val2 = arr2[j]
        if k < len3:
            val3 = arr3[k]
        # If we exhaust all values, break
        if val1 == float("inf") and val2 == float("inf") and val3 == float("inf"):
            break
        
        # Case where arr1 is smallest
        if val1 <= val2 and val1 <= val3:
            if not res or res[-1] != val1:
                res.append(val1)
            i += 1
        # Case where arr2 is smallest
        elif val2 <= val1 and val2 <= val3:
            if not res or res[-1] != val2:
                res.append(val2)
            j += 1
        # Case where arr3 is smallest
        elif val3 <= val1 and val3 <= val2:
            if not res or res[-1] != val3:
                res.append(val3)
            k += 1
        
    return res

# T: O(M + N + O)
# S: O(M + N + O)

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
arr3 = [4, 7, 11, 14]

print(mergeSortedArrays(arr1, arr2, arr3))
print(nums1)  # [1]
