
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # This fails the last 2 test cases on Leetcode due to memory issues, but it is a valid solution.
        # Basically we want to do a version of quick sort, without sorting, called quick select.
        # You partition the elements and you will know where the element is relative to the pivot. 
        # If length - k is the pivot, then that's the answer.
        # If length - k is smaller than the pivot index, you keep call partition on everything to the left of the pivot index.
        # If length - k is larger than the pivot, call the partition on everything to the right of the pivot index. 
        # Partition with the pivot, putting all smaller elements to the left and all large elements to the right of the pivot
        def partition(start, end):
            pivot = nums[end]
            left = start
            for i in range(start, end):
                if nums[i] <= pivot:
                    # Swap the current element with the left pointer element
                    nums[left], nums[i] = nums[i], nums[left]
                    # Increment left
                    left += 1
            # Swap the pivot with the left pointer
            nums[left], nums[end] = nums[end], nums[left]
            # Return the partition index
            return left
        
        def quick_select():
            # Do quick select
            start = 0
            end = len(nums) - 1
            # Edge case for an array of size 1
            if len(nums) == 1:
                return nums[0]
            # Go through nums
            while nums:
                pi = partition(start, end)
                # If the partition index is equal to length - k, then we know that the partition index is the result.
                # We know this because if or instance, k = 2 and the length is 6, then we know that if the partition index is 4 (5th element)
                # then there must be 4 elements smaller than it, meaning that there is only 1 element larger, which means we have the 2nd largest element.
                if len(nums) - k == pi:
                    return nums[pi]
                # If the partition index is smaller than length - k, then we know the answer is somewhere to the left of the partition. 
                # Using the same example as before, if k = 2 and length is 6, but the partition index is 5 (6th element), then the partition is at the largest element.
                # Thus, the element is somewhere to the left of the partition.
                elif len(nums) - k < pi:
                    end = pi - 1
                # If the partition index is smaller than length - k, then we know the answer is somewhere to the right of the partition. 
                elif len(nums) - k > pi:
                    start = pi + 1
            
        def use_heap():
            # Put k elements into the minHeap.
            # Then for the rest of the elements, only insert it into the heap if it's larger than the smallest element in the heap. 
            # Pop the smallest element, insert this larger element.
            # Since this is a minheap, the smallest values are at the top of the heap. If there are k items in the heap, then the top element in the heap has to be the kth largest. 
            # Then return the top element from the heap, this is the kth largest value. 
            heap = []
            for num in nums:
                # If the heap is smaller than size k, push onto the heap
                if len(heap) < k:
                    heapq.heappush(heap, num)
                else:
                    # If the heap's size is k and the current value is larger than the smallest value in the heap
                    # Pop from the heap and push this one on.
                    if num > heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, num)
            # Kth largest is the first element in the heap
            return heap[0]
            
        return use_heap()

        # T: O(NlogK) - Have to loop through nums and heappush is O(logK)
        # S: O(K) - we store K items. 