# To do this we need to find the misplaced index first, which is a value that is larger than its right neighbor. 
# Once we find the misplaced index, we need to find where that misplaced index is supposed to be (correct_index)
# Once we have both, we have to put the misplaced index in its correct place.
# To do that, we have to take the misplaced index out and push all values down by 1 until we're at the correct_index - 1. 
# Then for the last spot, we put the misplaced value. 
def fix_sorted_array(arr):
    n = len(arr)
    misplaced_index = -1
    correct_index = -1

    # Find the misplaced element and its correct position
    for i in range(n - 1):
        # Because we have a sorted array, if any element is larger than the next, it is out of place. 
        if arr[i] > arr[i + 1]:
            misplaced_index = i
            correct_index = i + 1
            # Once we've found the misplaced index, we need to find the correct index
            # Keep comparing misplaced index with next values until we find an index with a larger value.
            while correct_index < n and arr[misplaced_index] > arr[correct_index]:
                correct_index += 1
            break

    # If no misplaced element found, the array is already sorted
    if misplaced_index == -1:
        return arr

    # Move the misplaced element to its correct position
    misplaced_element = arr[misplaced_index]
    # We have to move all values up 1
    for i in range(misplaced_index, correct_index - 1):
        arr[i] = arr[i + 1]
    # Misplaced element is in the last spot. 
    arr[correct_index - 1] = misplaced_element

    return arr

# T: O(N) - even in the worst case, where the misplaced and correct values are an entire array length apart, we really only need to traverse the entire array once. 
# S: O(1) - only keep 2 pointers. 

arr = [2, 6, 3, 4, 7, 9]
print(fix_sorted_array(arr))
