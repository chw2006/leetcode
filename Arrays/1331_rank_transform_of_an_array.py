class Solution:
    # Put the elements and its index into a minHeap. 
    # Keep track of the rank as well as the previous value seen. 
    # Pop from the heap until it is empty. 
    # If the current value is larger than previous value, increment the rank. 
    # If not, rank stays the same, put that rank in the given index. 
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = 0
        prev_val = float('-inf')
        res = [0] * len(arr)
        # Go through the array and insert a tuple in-place (val, index)
        for i, val in enumerate(arr):
            arr[i] = (val, i)
        # Heapify the arr
        heapq.heapify(arr)
        # Pop from the heap until it's empty
        while arr:
            # Get val, index from heap
            val, index = heapq.heappop(arr)
            # If the current val is not the same as previous, we can increase the rank
            if val != prev_val:
                rank += 1
            # Put the rank at index in the res
            res[index] = rank
            # Update prev_val
            prev_val = val
        return res

# T: O(NlogN) - Enumerate and heapify are both O(N) operations. Popping from heap until it's empty is O(NlogN).
# S: O(N) - We make a copy of the array for the result


        