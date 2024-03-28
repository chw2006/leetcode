import heapq

class Solution:
    # We want to always pick the largest pile in piles so we get the minimum value at the end.
    # So we want to put the values in piles into a maxHeap (so we can pop max values from it)
    # Then for k times, we want to pop from the heap, divide it by 2, then push that value back onto the heap. 
    # After doing that k times, take the sum of the maxHeap. 
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # Create the maxHeap
        max_heap = [-x for x in piles]
        heapq.heapify(max_heap)
        # Do k operations
        for i in range(k):
            # Pop the largest value from the heap
            pile = heapq.heappop(max_heap)
            # Divide it by 2 (round down) and add it back to the heap
            heapq.heappush(max_heap, (pile // 2))
        # We want to sum the values in the heap, but since it is all negatives, we need to invert it when we return
        return -(sum(max_heap))
    # T: O(N + KlogN): Heapfiy takes O(N). We go through the loop k times and each time, we pop and push onto the heap, which are both O(logN) operations. Summing takes O(N).
    # S: O(N): we keep a heap